# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense , Dropout , GRU , Bidirectional
from keras.optimizers import SGD
import math
from sklearn.metrics import mean_squared_error

# DATASET
# https://www.kaggle.com/szrlee/stock-time-series-20050101-to-20171231

# loading data
data = pd.read_csv('./IBM_2006-01-01_to_2018-01-01.csv' , 
                  index_col = 'Date' , parse_dates=['Date'])

# splitting the data 
training_set = data[:'2016'].iloc[:,1:2].values
test_set = data['2017':].iloc[:,1:2].values

# scaling the training set
sc = MinMaxScaler(feature_range = (0,1))
training_set_scaled = sc.fit_transform(training_set)

# Since GRU's store long term memory state, we create a data structure with 60 timesteps and 1 output
# So for each element of training set, we have 60 previous training set elements 
x_train = []
y_train = []
for i in range(60,2769):
    x_train.append(training_set_scaled[i-60:i,0])
    y_train.append(training_set_scaled[i , 0])
    
x_train , y_train = np.array(x_train) , np.array(y_train)

# reshaping x_train
x_train = np.reshape(x_train , (x_train.shape[0]  , x_train.shape[1] , 1))


class gru_model():
	def return_rmse(self , test , predicted):
		# evaluating the model
	    rmse = math.sqrt(mean_squared_error(test , predicted))
	    print("The root mean squared error is {}.".format(rmse))

	def predict(self):
		# compiling the whole data
		dataset_total = pd.concat((data["High"][:'2016'],data["High"]['2017':]),axis=0)
		inputs = dataset_total[len(dataset_total)-len(test_set) - 60:].values

		# reshaping 
		inputs = inputs.reshape(-1,1)

		# scaling
		inputs  = sc.transform(inputs)

		# converting data to appropriate form
		x_test = []
		for i in range(60 , 311):
		    x_test.append(inputs[i-60:i , 0])
		x_test = np.array(x_test)

		# reshape
		x_test = np.reshape(x_test , (x_test.shape[0] , x_test.shape[1] , 1))

		# predicting result
		predicted_stock_price = model.predict(x_test)

		# inverse transformation
		predicted_stock_price = sc.inverse_transform(predicted_stock_price)
		return predicted_stock_price


	def get_model(self):
		# Initializing the network
		regressor = Sequential()

		# adding first gru layer 
		regressor.add(GRU(units = 50 , return_sequences = True , input_shape = (x_train.shape[1] , 1) , activation = 'tanh'))
		regressor.add(Dropout(0.2))
		
		# adding second gru layer
		regressor.add(GRU(units = 50 , return_sequences = True , input_shape = (x_train.shape[1],1) , activation='tanh'))
		regressor.add(Dropout(0.2))

		# adding third gru layer
		regressor.add(GRU(units = 50 , return_sequences = True , input_shape = (x_train.shape[1],1) , activation='tanh'))
		regressor.add(Dropout(0.2))

		# adding fourth gru layer
		regressor.add(GRU(units = 50 , activation='tanh'))
		regressor.add(Dropout(0.2))

		# adding the output layer
		regressor.add(Dense(units = 1))

		return regressor




gru = gru_model()

model = gru.get_model()

# compiling the network
model.compile(optimizer = SGD(lr = 0.01 , decay = 1e-7 , momentum = 0.9 , nesterov = False) , loss = 'mean_squared_error')

# fitting the data to the model
model.fit(x_train,y_train , epochs = 50 , batch_size = 150)

# predicting stock price
predicted_stock_price = gru.predict()

# print root mean squared error
gru.return_rmse(test_set , predicted_stock_price)