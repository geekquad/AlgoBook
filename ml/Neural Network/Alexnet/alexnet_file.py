import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPool2D, InputLayer, Dense, BatchNormalization, Flatten, ZeroPadding2D,Activation, Dropout

def alexnet_model(inputshape, num_outputs):
    alexnet_model = tf.keras.Sequential([InputLayer(input_shape= inputshape),
                                
                                #layer1
                                Conv2D(48,(11,11), strides = (2,2)),
                                BatchNormalization(),
                                Activation("relu"),
                                MaxPool2D(pool_size=(3, 3),strides=(2,2)),
                                
                                #layer2
                                Conv2D(128,(5,5),strides = (1,1), padding = "same"),
                                BatchNormalization(),
                                Activation("relu"),
                                MaxPool2D(pool_size=(3, 3), strides=(2,2)),
                                
                                #layer3
                                Conv2D(192,(3,3),strides = (1,1), padding = "same"),
                                BatchNormalization(),
                                Activation("relu"),
                                
                                #layer4
                                Conv2D(192,(3,3),strides = (1,1), padding = "same"),
                                BatchNormalization(),
                                Activation("relu"),
                                
                                #layer5
                                Conv2D(128,(3,3),strides = (1,1), padding = "same"),
                                BatchNormalization(),
                                Activation("relu"),
                                MaxPool2D(pool_size= (3, 3),strides=(2,2)),
                                
                                Flatten(),
                                
                                #layer6
                                Dense(1024, ),
                                BatchNormalization(),
                                Activation("relu"),
                                #Dropout(0.9),
                                
                                #layer7
                                Dense(1024, ),
                                BatchNormalization(),
                                Activation("relu"),
                                #Dropout(0.9),
                                
                                #layer8
                                Dense(num_outputs, ),
                                BatchNormalization(),
                                Activation("softmax"),
                                

    ])

    tf.keras.utils.plot_model(alexnet_model, to_file='alexnet.png', show_shapes=True) #saving the model architecture in an image form

    alexnet_model.compile(loss= "categorical_crossentropy",optimizer= "adam",metrics = ["accuracy"])
    return alexnet_model
