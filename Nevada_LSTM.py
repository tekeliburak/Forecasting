df1 = pd.read_csv('NevadaTrain.csv')
Train = df1[:1029246]
Test = df1[1029246:]
azimut_rad_train = Train.pop('Azimuth Angle')*np.pi / 180
zenith_rad_train = Train.pop('Zenith Angle')*np.pi/180
datatrain = pd.concat([Train, azimut_rad_train, zenith_rad_train], axis=1)
newdatatrain = datatrain[datatrain['Global Horiz'] > 0]
newdatatrain = newdatatrain[newdatatrain['Dry Bulb Temp'] < 60]
newdatatrain = newdatatrain[newdatatrain['Dry Bulb Temp'] > -10]
newdatatrain = newdatatrain[newdatatrain['BB Aerosol Optical Depth'] > -20000]
X_train = newdatatrain[['Dry Bulb Temp','Wind Chill Temp','Dew Point Temp','Rel Humidity','Avg Wind Speed',
 'Peak Wind Speed', 'Avg Wind Direction','Precipitationx','Precipitation',
 'BB Aerosol Optical Depth','Zenith Angle','Azimuth Angle','Airmass','CR10X Temp','CR10X Battery']]
Y_train = newdatatrain[['Global Horiz']]
azimut_rad_test = Test.pop('Azimuth Angle')*np.pi / 180
zenith_rad_test = Test.pop('Zenith Angle')*np.pi/180
datatest = pd.concat([Test, azimut_rad_test, zenith_rad_test], axis=1)
newdatatest = datatest[datatest['Global Horiz'] > 0]
X_test = newdatatest[['Dry Bulb Temp', 'Wind Chill Temp', 'Dew Point Temp', 
'Rel Humidity', 'Avg Wind Speed',
 'Peak Wind Speed', 'Avg Wind Direction', 
'Precipitationx', 'Precipitation',
 'BB Aerosol Optical Depth', 'Zenith Angle', 'Azimuth Angle', 'Airmass', 'CR10X Temp', 'CR10X Battery']]
Y_test = newdatatest['Global Horiz']
LSTMmodel(X_train, Y_train, X_test, Y_test, 2000,10,32,"First 2000 Test Data","Irradiance")