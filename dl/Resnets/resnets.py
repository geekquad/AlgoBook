import torch
import torch.nn as nn
import torch.nn.functional as F
import math

def conv3x3(in_planes, out_planes, stride=1):
    "3x3 convolution with padding"
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride,
                     padding=1, bias=False)


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, dim_change=None):
        super(BasicBlock, self).__init__()
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = nn.BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = nn.BatchNorm2d(planes)
        self.dim_change = dim_change
        self.stride = stride

    def forward(self, x):
        residual = x

        output = self.conv1(x)
        output = self.bn1(output)
        output = F.relu(output)

        output = self.conv2(output)
        output = self.bn2(output)

        if self.dim_change is not None:
            residual = self.dim_change(x)

        output += residual
        output = F.relu(output)

        return output


class Bottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1, downsample=None):
        super(Bottleneck, self).__init__()
        self.conv1 = nn.Conv2d(
            inplanes,
            planes,
            kernel_size=1,
            stride=stride,
            bias=False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, stride=1,
                               padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(planes, planes * expansion,
                               kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(planes * expansion)
        self.relu = nn.ReLU(inplace=True)
        self.dim_change = dim_change
        self.stride = stride

    def forward(self, x):
        residual = x

        output = self.conv1(x)
        output = self.bn1(output)
        output = F.relu(output)

        output = self.conv2(output)
        output = self.bn2(output)
        output = F.relu(output)

        output = self.conv3(output)
        output = self.bn3(output)

        if self.dim_change is not None:
            residual = self.dim_change(x)

        output += residual
        output = F.relu(output)

        return output


class ResNet(nn.Module):

    def __init__(self, block, layers, num_classes=1000):

        super(ResNet, self).__init__()
        # according to research paper:
        self.input_planes = 64
        self.conv1 = torch.nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(64)
        self.layer1 = self._layer(block, 64, num_layers[0], stride=1)
        self.layer2 = self._layer(block, 128, num_layers[1], stride=2)
        self.layer3 = self._layer(block, 256, num_layers[2], stride=2)
        self.layer4 = self._layer(block, 512, num_layers[3], stride=2)
        self.averagePool = torch.nn.AvgPool2d(kernel_size=4, stride=1)
        self.fc = torch.nn.Linear(512 * block.expansion, classes)

    def _layer(self, block, planes, blocks, stride=1):

        dim_change = None
        if stride != 1 or planes != self.input_planes * block.expansion:
            dim_change = nn.Sequential(
                nn.Conv2d(self.input_planes, planes * block.expansion,
                          kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(planes * block.expansion)
            )
        netLayers = []
        netLayers.append(block(self.inplanes, planes,
                               stride=stride, dim_change=dim_change))
        self.inplanes = planes * block.expansion
        for i in range(1, blocks):
            netLayers.append(block(self.input_planes, planes))
            self.inplanes = planes * block.expansion

        return nn.Sequential(*netLayers)


def resnet18():

    model = ResNet(BasicBlock, [2, 2, 2, 2])
    return model


def resnet34():

    model = ResNet(BasicBlock, [3, 4, 6, 3])
    return model


def resnet50():

    model = ResNet(Bottleneck, [3, 4, 6, 3])
    return model


def resnet101():

    model = ResNet(Bottleneck, [3, 4, 23, 3])
    return model


def resnet152():

    model = ResNet(Bottleneck, [3, 8, 36, 3])
    return model
