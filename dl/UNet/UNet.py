import os
import random
import numpy as np
from tqdm import tqdm
import tensorflow as tf
from skimage.io import imread,imshow
from skimage.transform import resize
import matplotlib.pyplot as plt


# Data Preprocessing
TRAIN_PATH="stage1_train/"
TEST_PATH='stage1_test/'

train_ids=next(os.walk(TRAIN_PATH))[1]
test_ids=next(os.walk(TEST_PATH))[1]

IMG_HEIGHT=128
IMG_WIDTH=128
IMG_CHANNELS=3

X_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
Y_train = np.zeros((len(train_ids), IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.bool)

print('Resizing training images and masks')
for n, id_ in tqdm(enumerate(train_ids), total=len(train_ids)):   
    path = TRAIN_PATH + id_
    img = imread(path + '/images/' + id_ + '.png')[:,:,:IMG_CHANNELS]  
    img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
    X_train[n] = img  #Fill empty X_train with values from img
    mask = np.zeros((IMG_HEIGHT, IMG_WIDTH, 1), dtype=np.bool)
    for mask_file in next(os.walk(path + '/masks/'))[2]:
        mask_ = imread(path + '/masks/' + mask_file)
        mask_ = np.expand_dims(resize(mask_, (IMG_HEIGHT, IMG_WIDTH), mode='constant',  
                                      preserve_range=True), axis=-1)
        mask = np.maximum(mask, mask_)  
            
    Y_train[n] = mask   

# test images
X_test = np.zeros((len(test_ids), IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS), dtype=np.uint8)
sizes_test = []
print('Resizing test images') 
for n, id_ in tqdm(enumerate(test_ids), total=len(test_ids)):
    path = TEST_PATH + id_
    img = imread(path + '/images/' + id_ + '.png')[:,:,:IMG_CHANNELS]
    sizes_test.append([img.shape[0], img.shape[1]])
    img = resize(img, (IMG_HEIGHT, IMG_WIDTH), mode='constant', preserve_range=True)
    X_test[n] = img

print('Done!')

########################################################################

class unet_model():
	def get_model(self):
		#Build the model
		inputs = tf.keras.layers.Input((IMG_HEIGHT, IMG_WIDTH, IMG_CHANNELS))
		s = tf.keras.layers.Lambda(lambda x: x / 255)(inputs)

		#Contraction path
		c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(s)
		c1 = tf.keras.layers.Dropout(0.1)(c1)
		c1 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c1)
		p1 = tf.keras.layers.MaxPooling2D((2, 2))(c1)

		c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p1)
		c2 = tf.keras.layers.Dropout(0.1)(c2)
		c2 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c2)
		p2 = tf.keras.layers.MaxPooling2D((2, 2))(c2)
		 
		c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p2)
		c3 = tf.keras.layers.Dropout(0.2)(c3)
		c3 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c3)
		p3 = tf.keras.layers.MaxPooling2D((2, 2))(c3)
		 
		c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p3)
		c4 = tf.keras.layers.Dropout(0.2)(c4)
		c4 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c4)
		p4 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(c4)
		 
		c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(p4)
		c5 = tf.keras.layers.Dropout(0.3)(c5)
		c5 = tf.keras.layers.Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c5)

		#Expansive path 
		u6 = tf.keras.layers.Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(c5)
		u6 = tf.keras.layers.concatenate([u6, c4])
		c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u6)
		c6 = tf.keras.layers.Dropout(0.2)(c6)
		c6 = tf.keras.layers.Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c6)
		 
		u7 = tf.keras.layers.Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(c6)
		u7 = tf.keras.layers.concatenate([u7, c3])
		c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u7)
		c7 = tf.keras.layers.Dropout(0.2)(c7)
		c7 = tf.keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c7)
		 
		u8 = tf.keras.layers.Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(c7)
		u8 = tf.keras.layers.concatenate([u8, c2])
		c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u8)
		c8 = tf.keras.layers.Dropout(0.1)(c8)
		c8 = tf.keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c8)
		 
		u9 = tf.keras.layers.Conv2DTranspose(16, (2, 2), strides=(2, 2), padding='same')(c8)
		u9 = tf.keras.layers.concatenate([u9, c1], axis=3)
		c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(u9)
		c9 = tf.keras.layers.Dropout(0.1)(c9)
		c9 = tf.keras.layers.Conv2D(16, (3, 3), activation='relu', kernel_initializer='he_normal', padding='same')(c9)
		 
		outputs = tf.keras.layers.Conv2D(1, (1, 1), activation='sigmoid')(c9)
		model = tf.keras.Model(inputs=[inputs], outputs=[outputs])
		model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
		model.summary()

		return model

#callbacks
callbacks=[tf.keras.callbacks.EarlyStopping(patience=2,monitor='val_loss'),
           tf.keras.callbacks.TensorBoard(log_dir='logs')]


unet = unet_model()
model = unet.get_model()

#training model
results=model.fit(X_train,Y_train,validation_split=0.1,batch_size=16,epochs=30,callbacks=callbacks)

#predicting test_data
predict_test=model.predict(X_test,verbose=1)
predict_test_t=(predict_test>0.5).astype(np.uint8)

#showing predicted output
imshow(X_test[1])
plt.show()
imshow(np.squeeze(predict_test_t[1]))
plt.show()