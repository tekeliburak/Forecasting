data = pd.read_csv('/content/drive/MyDrive/data/ConsumptionData.csv')
data_new = pd.get_dummies(data, columns=['type','week'])
a = data_new.iloc[:14616,:]
b = data_new.iloc[14616:,:]
new_train = a.sample(frac=1).reset_index(drop=True)
X_train = new_train.iloc[:,3:]
Y_train = new_train.iloc[:,2:3]
X_test = b.iloc[:,3:]
Y_test = b.iloc[:,2:3]
LSTMmodel(X_train, Y_train, X_test, Y_test, 200,90,4,"First 200 Test Data","Consumption (kW)")