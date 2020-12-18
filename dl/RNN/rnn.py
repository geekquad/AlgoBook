import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

def rnn_model(input_shape, x_train, y_train, x_test, y_test, epochs=0, loss='sparse_categorical_crossentropy', metric='accuracy', lr=0):
    model = Sequential([

            LSTM(128, input_shape=input_shape, activation='relu', return_sequences=True),
            Dropout(0.2),

            LSTM(128, activation='relu'), 
            Dropout(0.2),

            Dense(32, activation='relu'),
            Dropout(0.2),

            Dense(10, activation='softmax')

        ])
    print(model.summary())


    optimizer = tf.keras.optimizers.Adam(lr=lr, decay=0.00005)
    model.compile(loss=loss, 
            optimizer=optimizer, 
            metrics=[metric])

    model.fit(x_train, y_train, epochs=epochs, validation_data=(x_test, y_test))


# example
# rnn_model((28, 28),x_train, y_train, x_test, y_test, epochs=5, loss='sparse_categorical_crossentropy', metric='accuracy', lr=0.01)