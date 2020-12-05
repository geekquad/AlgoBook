import torch
import torch.nn as nn
from torchvision import datasets, transforms

IMAGES_PATH = 'image_path'

transform = transforms.Compose([transforms.Resize(256),
                                transforms.RandomCrop(224),
                                transforms.ToTensor()])

trainset = datasets.ImageFolder(IMAGES_PATH+str('train/'), transform=transform)
testset = datasets.ImageFolder(IMAGES_PATH+str('test/'), transform=transform)

trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=True)

class VGG16(nn.Module):
    
    def __init__(self, features):
        self.features = features
        self.classifier = nn.Sequential(
            nn.Linear(512*7*7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 1000)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

arc = [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 
       512, 512, 512, 'M', 512, 512, 512, 'M']

def make_features(arc):
    layers = []
    in_channels = 3
    for i in arc:
        if i == 'M':
            layers += [nn.MaxPool2d(2, 2)]
        else:
            conv = nn.Conv2d(in_channels, i, 3, padding=1)
            layers += [conv, nn.BatchNorm2d(i), nn.ReLU(True)]
            in_channels = i
    return nn.Sequential(*layers)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = VGG16(make_features(arc))
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for e in range(10):
    for images, labels in trainloader:
        
        images, labels = images.to(device), labels.to(device)
        
        outputs = model(images)
        
        loss = criterion(outputs, labels)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    print(f'Epoch: {e+1}, Loss: {loss.item()}')

model.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in testloader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    
    print(f'Accuracy: {100 * correct / total:.4f}')