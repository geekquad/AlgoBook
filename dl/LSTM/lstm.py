
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dropout, Dense, LSTM
from keras.optimizers import Adam
print("Import Successful!!")

#loading data
(x_train , y_train) , (x_test , y_test) = mnist.load_data()

#normalizing data
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

class lstm_model():
    def setup(self):
        #Initializing the classifier Network
        classifier = Sequential()

        #Adding the input LSTM network layer
        classifier.add(LSTM(128, input_shape=(x_train.shape[1:]), return_sequences=True))
        classifier.add(Dropout(0.2))
        
        #Adding a second LSTM network layer
        classifier.add(LSTM(128))

        #Adding a dense hidden layer
        classifier.add(Dense(64, activation='relu'))
        classifier.add(Dropout(0.2))

        #Adding the output layer
        classifier.add(Dense(10, activation='softmax'))
        
        return classifier;


lstm = lstm_model()
model = lstm.setup()
#Compiling the network
model.compile( loss='sparse_categorical_crossentropy',
              optimizer=Adam(lr=0.001, decay=1e-6),
              metrics=['accuracy'] )


#Fitting the data to the model
model.fit(x_train,
         y_train,
          epochs=3,
          validation_data=(x_test, y_test))


test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test Loss: {}'.format(test_loss))
print('Test Accuracy: {}'.format(test_acc))