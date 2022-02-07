import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
datatrain = pd.read_csv('solartacTrain.csv')
azimut_rad_train = datatrain.pop('Azimuth Angle [degrees]')*np.pi / 180
zenith_rad_train = datatrain.pop('Zenith Angle [degrees]')*np.pi/180
avgwind_rad_train = datatrain.pop('Avg Wind Direction @ 10m [deg from N]')*np.pi/180
datatrain = pd.concat([datatrain,azimut_rad_train,zenith_rad_train,avgwind_rad_train],axis=1)
names = datatrain.columns.tolist()
names[names.index('Azimuth Angle [degrees]')] = 'Azimuth Angle [Radians]'
names[names.index('Zenith Angle [degrees]')] = 'Zenith Angle [Radians]'
names[names.index('Avg Wind Direction @ 10m [deg from N]')] = 'Avg Wind Direction @ 10m [Radians from N]'
datatrain.columns = names
newdatatrain = datatrain[datatrain['Global Horizontal [W/m^2]'] > 0]
newdatatrain = newdatatrain[newdatatrain['Air Temperature [deg C]'] > -2000]
X_train = newdatatrain[['Air Temperature [deg C]','Wind Chill Temp [deg C]','Dew Point Temp [deg C]','Rel Humidity [%]',
 'Avg Wind Speed @ 10m [m/s]','Peak Wind Speed @ 10m [m/s]','Avg Wind Direction @ 10m [Radians from N]',
 'Precipitation [mm]','Precipitation (Accumulated) [mm]','Zenith Angle [Radians]','Azimuth Angle [Radians]',
 'CR1000 Temp [deg C]','CR1000 Battery [VDC]']]
Y_train = newdatatrain[['Global Horizontal [W/m^2]']]
datatest = pd.read_csv('solartacTest.csv')
azimut_rad_test = datatest.pop('Azimuth Angle [degrees]')*np.pi / 180
zenith_rad_test = datatest.pop('Zenith Angle [degrees]')*np.pi/180
avgwind_rad_test = datatest.pop('Avg Wind Direction @ 10m [deg from N]')*np.pi/180
datatest = pd.concat([datatest,azimut_rad_test,zenith_rad_test,avgwind_rad_test],axis=1)
names = datatest.columns.tolist()
names[names.index('Azimuth Angle [degrees]')] = 'Azimuth Angle [Radians]'
names[names.index('Zenith Angle [degrees]')] = 'Zenith Angle [Radians]'
names[names.index('Avg Wind Direction @ 10m [deg from N]')] = 'Avg Wind Direction @ 10m [Radians from N]'
datatest.columns = names
newdatatest = datatest[datatest['Global Horizontal [W/m^2]'] > 0]
X_test = newdatatest[['Air Temperature [deg C]','Wind Chill Temp [deg C]','Dew Point Temp [deg C]','Rel Humidity [%]',
 'Avg Wind Speed @ 10m [m/s]','Peak Wind Speed @ 10m [m/s]','Avg Wind Direction @ 10m [Radians from N]',
 'Precipitation [mm]','Precipitation (Accumulated) [mm]','Zenith Angle [Radians]','Azimuth Angle [Radians]',
 'CR1000 Temp [deg C]','CR1000 Battery [VDC]']]
Y_test = newdatatest['Global Horizontal [W/m^2]']
decision_tree_regression(X_train, Y_train, X_test, Y_test, 2000)
linear_regression(X_train, Y_train, X_test, Y_test.to_frame(), 2000)
xgboost_regression(X_train.values, Y_train.values, X_test.values, Y_test.values, 2000)
#
x = newdatatest[['Air Temperature [deg C]','Wind Chill Temp [deg C]','Dew Point Temp [deg C]','Rel Humidity [%]',
 'Avg Wind Speed @ 10m [m/s]','Peak Wind Speed @ 10m [m/s]','Avg Wind Direction @ 10m [Radians from N]',
 'Precipitation [mm]','Precipitation (Accumulated) [mm]','Zenith Angle [Radians]','Azimuth Angle [Radians]',
 'CR1000 Temp [deg C]','CR1000 Battery [VDC]']]
corr = np.round(x.corr(), 2)
fig, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(ax=ax,
 data=corr,
 annot=True,
 cmap="coolwarm",
 vmin=-1, vmax=1, center=0)
ax.set_title("Correlation Matrix Graph")
plt.yticks(rotation=0)
plt.show()
cor_target = abs(corr['Global Horizontal [W/m^2]'])
