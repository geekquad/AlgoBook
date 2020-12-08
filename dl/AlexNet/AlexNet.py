#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dense,Input,Dropout,Flatten, Conv2D
from tensorflow.keras.layers import BatchNormalization,Activation, MaxPooling2D
from tensorflow.keras.models import Model,Sequential
from tensorflow.keras.optimizers import Adam


# In[18]:


images_location='/home/pranshul/mask_recognition/mask-recognition'
img_size=227
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


# In[19]:


model=Sequential()

#1st convolution layer
model.add(Conv2D(96,(11,11),padding='valid',strides=4,input_shape=(227,227,3)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3,3),strides=2))

model.add(Conv2D(256,(5,5),padding='same'))
model.add(BatchNormalization())
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(3,3),strides=2))

model.add(Conv2D(384,(3,3),padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(384,(3,3),padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))

model.add(Conv2D(256,(3,3),padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3,3),strides=2))

model.add(Flatten())

model.add(Dense(4096))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(4096))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(2,activation='softmax'))
model.compile(optimizer=Adam(lr=0.005),loss="categorical_crossentropy",metrics=['accuracy'])
model.summary()


# In[20]:


get_ipython().run_cell_magic('time', '', '\nepochs=20\nsteps_per_epoch=train_generator.n//train_generator.batch_size\nvalidation_steps = validation_generator.n//validation_generator.batch_size\nhistory= model.fit(x=train_generator,epochs=epochs,steps_per_epoch=steps_per_epoch,validation_data=validation_generator,\n                  validation_steps=validation_steps)\nscoreSeg = model.evaluate_generator(validation_generator)\nprint("Accuracy = ",scoreSeg[1]*100)')


# In[ ]:




