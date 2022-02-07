df1 = pd.read_csv('/content/drive/MyDrive/data/all9dot.csv') # Read Train Data set from csv file for 9 locations
df2 = pd.read_csv('/content/drive/MyDrive/data/all9dot_2019.csv') # Read Test Data set from csv file 9 locations
newdatatrain = df1[df1['electricity'] > 0]
X_train = newdatatrain.iloc[:,3:]
Y_train = newdatatrain.iloc[:,2:3]
newdatatest = df2[df2['electricity'] > 0]
X_test = newdatatest.iloc[:,3:]
Y_test = newdatatest.iloc[:,2:3]
LSTMmodel(X_train, Y_train, X_test, Y_test, 200, 20,128,"First 200 Data Test Values","Electricity(kW)" )
