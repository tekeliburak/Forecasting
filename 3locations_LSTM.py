df1 = pd.read_csv('/content/drive/MyDrive/data/all9dot.csv') # Read Train Data set from csv file for 9 locations
df2 = pd.read_csv('/content/drive/MyDrive/data/all9dot_2019.csv') # Read Test Data set from csv file 9 locations
df1_new = df1.iloc[105192:210384] # 105192:210384 for 3 locations Train Data set
df2_new = df2[26280:52560] # 26280:52560 for 3 locations Test Data set
newdatatrain = df1_new[df1_new['electricity'] > 0]
X_train = newdatatrain.iloc[:,3:]
Y_train = newdatatrain.iloc[:,2:3]
newdatatest = df2_new[df2_new['electricity'] > 0]
X_test = newdatatest.iloc[:,3:]
Y_test = newdatatest.iloc[:,2:3]
LSTMmodel(X_train, Y_train, X_test, Y_test, 200, 20,128,"First 200 Data Test Values","Electricity(kW)" )
