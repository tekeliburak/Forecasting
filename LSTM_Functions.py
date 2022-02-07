import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional
import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
def MAPE(Y_actual,Y_Predicted):
 mape = np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100
 return mape
def LSTMmodel(X_train, Y_train, X_test, Y_test, data_value, EPOCHS, 
BATCH_SIZE, XLabel, YLabel):
 sc = MinMaxScaler(feature_range=(0, 1))
 training_set_scaledX = sc.fit_transform(X_train)
 training_set_scaledY = sc.fit_transform(Y_train)
 X_train_new, Y_train_new = np.array(training_set_scaledX), np.array(training_set_scaledY)
 regressor = Sequential()
 regressor.add(LSTM(units=50, return_sequences=True, input_shape=(X_train_new.shape[1], 1)))
 regressor.add(Dropout(0.2))
 regressor.add(LSTM(units=50, return_sequences=True))
 regressor.add(Dropout(0.2))
 regressor.add(LSTM(units=50, return_sequences=True))
 regressor.add(Dropout(0.2))
 regressor.add(LSTM(units=50))
 regressor.add(Dropout(0.2))
 regressor.add(Dense(units=1, activation="sigmoid"))
 regressor.compile(optimizer='rmsprop', loss='mean_squared_error')
 regressor.fit(X_train_new, Y_train_new, epochs=EPOCHS, batch_size=BATCH_SIZE)
 test_set_scaledX = sc.fit_transform(X_test)
 X_test_new = np.array(test_set_scaledX)
 a = regressor.predict(X_test_new)
 test_set_scaledY = sc.fit_transform(Y_test)
 Y_test_new = np.array(test_set_scaledY)
 Y_pred = sc.inverse_transform(a)
 print('LSTM:')
 print(f'MSE: {mean_squared_error(Y_test.values, Y_pred)}')
 print(f'RMSE: {math.sqrt(mean_squared_error(Y_test.values, Y_pred))}')
 print(f'MAPE: {MAPE(Y_test.values, Y_pred)}')
 print(f'MAE: {mean_absolute_error(Y_test.values, Y_pred)}')
 plt.figure(figsize=(10, 7))
 plt.subplot(211)
 plt.xlabel(XLabel)
 plt.ylabel(YLabel)
 plt.plot(range(data_value), Y_test[0:data_value], 'bo', label="Actual Value")
 plt.plot(range(data_value), Y_pred[0:data_value], 'ro', label="Predict Value")
 plt.title(f'LSTM: Train Data = {len(Y_train)} Test Data = {len(Y_test)}')
 plt.legend()
 plt.subplot(212)
 plt.xlabel(XLabel)
 plt.ylabel(YLabel)
 plt.plot(range(data_value), Y_test[0:data_value], 'b', label="Actual Value")
 plt.plot(range(data_value), Y_pred[0:data_value], 'r', label="Predict Value")
 plt.legend()
 plt.show()
