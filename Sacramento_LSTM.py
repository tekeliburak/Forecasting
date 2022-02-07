datatrain = pd.read_csv('Sacramento_train.csv')
zenith_rad_train = datatrain.pop('Zenith Angle [degrees]')*np.pi/180
datatrain = pd.concat([datatrain,zenith_rad_train],axis=1)
names = datatrain.columns.tolist()
names[names.index('Zenith Angle [degrees]')] = 'Zenith Angle [Radians]'
datatrain.columns = names
newdatatrain = datatrain[datatrain['Global Horizontal [W/m^2]'] > 0]
newdatatrain = newdatatrain[newdatatrain['Station Pressure [mBar]'] > 800]
newdatatrain = newdatatrain[newdatatrain['CR1000 Temp [deg C]'] > -2000]
newdatatrain = newdatatrain[newdatatrain['RSR Battery [VDC]'] > 2]
X_train = newdatatrain[['Air Temperature [deg C]','Rel Humidity [%]','Station Pressure [mBar]','Zenith Angle [Radians]',
 'CR1000 Temp [deg C]','RSR Battery [VDC]']]
Y_train = newdatatrain[['Global Horizontal [W/m^2]']]
datatest = pd.read_csv('Sacramento_test.csv')
zenith_rad_test = datatest.pop('Zenith Angle [degrees]')*np.pi/180
datatest = pd.concat([datatest,zenith_rad_test],axis=1)
names = datatest.columns.tolist()
names[names.index('Zenith Angle [degrees]')] = 'Zenith Angle [Radians]'
datatest.columns = names
newdatatest = datatest[datatest['Global Horizontal [W/m^2]'] > 0]
X_test = newdatatest[['Air Temperature [deg C]','Rel Humidity [%]','Station Pressure [mBar]','Zenith Angle [Radians]',
 'CR1000 Temp [deg C]','RSR Battery [VDC]']]
Y_test = newdatatest['Global Horizontal [W/m^2]']
LSTMmodel(X_train, Y_train, X_test, Y_test, 2000,10,32,"First 2000 Test Data","Irradiance")