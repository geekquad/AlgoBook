import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense,Input,Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization,Activation, MaxPooling2D
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.optimizers import Adam

images_location='/home/pranshul/mask_recognition/mask-recognition'                    #Enter the image location here
img_size=224
batch_size=64

datagen_train = ImageDataGenerator(horizontal_flip=True)
train_generator=datagen_train.flow_from_directory(images_location+'/'+'train/',
                                                  target_size=(img_size,img_size),
                                                  color_mode='rgb',
                                                  batch_size=batch_size,
                                                  shuffle=True
                                                 )

datagen_validation = ImageDataGenerator(horizontal_flip=True)
validation_generator=datagen_validation.flow_from_directory(images_location+'/'+"test/",
                                                      target_size=(img_size,img_size),
                                                      color_mode="rgb",
                                                      batch_size=batch_size,
                                                      shuffle=True
                                                     )


num_output_classes=2                                                                  #Enter the num_ouput_classes
class AlexNet:
    def setup(self):
        model=Sequential()

        #1st convolution layer
        model.add(Conv2D(filters=96,kernel_size=(11,11),padding='valid',strides=4,input_shape=(224,224,3)))
        model.add(Activation('relu'))
        #Maxpooling layer
        model.add(MaxPooling2D(pool_size=(3,3),strides=2))
        # batch normalization
        model.add(BatchNormalization())

        #2nd convolution layer
        model.add(Conv2D(filters=256,kernel_size=(5,5),strides=(1,1),padding='same'))
        model.add(Activation("relu"))
        #Maxpooling layer
        model.add(MaxPooling2D(pool_size=(3,3),strides=2))
        #batch normalization
        model.add(BatchNormalization())

        #3rd convolution layer
        model.add(Conv2D(filters=384,kernel_size=(3,3),strides=(1,1),padding='same'))
        model.add(Activation('relu'))
        #batch normalization
        model.add(BatchNormalization())

        #4th Convolution layer
        model.add(Conv2D(filters=384,kernel_size=(3,3),strides=(1,1),padding='same'))
        model.add(Activation('relu'))
        #Batch normalization
        model.add(BatchNormalization())

        #5th convolution layer
        model.add(Conv2D(filters=256,kernel_size=(3,3),strides=(1,1),padding='same'))
        model.add(Activation('relu'))
        #maxpooling
        model.add(MaxPooling2D(pool_size=(3,3),strides=2))
        #batch normalization
        model.add(BatchNormalization())

        #flattening
        model.add(Flatten())

        #1st Dense Layer
        model.add(Dense(4096))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(BatchNormalization())

        #2nd Dense layer
        model.add(Dense(4096))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))

        #adding output softmax layer
        model.add(Dense(num_output_classes,activation='softmax'))
        return model;


alexnet=AlexNet()                                   # calling the AlexNet 
model=alexnet.setup()                               
model.compile(optimizer=Adam(lr=0.005),loss="categorical_crossentropy",metrics=['accuracy'])
model.summary()


epochs=2                                            #enter the number of epochs
steps_per_epoch=train_generator.n//train_generator.batch_size
validation_steps = validation_generator.n//validation_generator.batch_size
history= model.fit(x=train_generator,epochs=epochs,steps_per_epoch=steps_per_epoch,validation_data=validation_generator,
                  validation_steps=validation_steps)
scoreSeg = model.evaluate_generator(validation_generator)
print("Accuracy  = ",scoreSeg[1]*100)
