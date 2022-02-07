import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
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
decision_tree_regression(X_train, Y_train, X_test, Y_test, 2000)
linear_regression(X_train, Y_train, X_test, Y_test.to_frame(), 2000)
xgboost_regression(X_train.values, Y_train.values, X_test.values, Y_test.values, 2000)
x = newdatatrain[['Global Horizontal [W/m^2]','Air Temperature [deg C]','Rel Humidity [%]','Station Pressure [mBar]',
 'Zenith Angle [Radians]','CR1000 Temp [deg C]','RSR Battery [VDC]']]
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
