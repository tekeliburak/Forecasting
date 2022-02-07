import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# -------------------------------------------------------------------------
# ninja for 3 Locations
# -------------------------------------------------------------------------
df1 = pd.read_csv('all9dot.csv') # Read Train Data set from csv file for 9 locations
df2 = pd.read_csv('all9dot_2019.csv') # Read Test Data set from csv file 9 locations
df1_new = df1.iloc[105192:210384] # 105192:210384 for 3 locations Train Data set
df2_new = df2[26280:52560] # 26280:52560 for 3 locations Test Data set
X = df1_new[df1_new['electricity'] != 0] # Eliminate null values
X_train = X[['irradiance_direct', 'irradiance_diffuse', 'temperature', 
'precipitation', 'snowfall',
 'snow_mass', 'air_density', 'radiation_surface', 
'radiation_tao', 'cloud_cover']] # Independent Variables for Training Data
Y_train = X[['electricity']] # Dependent Variable for Training Data
Y = df2_new[df2_new['electricity'] != 0] # Eliminate null values
X_test = Y[['irradiance_direct', 'irradiance_diffuse', 'temperature', 
'precipitation', 'snowfall',
 'snow_mass', 'air_density', 'radiation_surface', 
'radiation_tao', 'cloud_cover']] # Independent Variables for Test Data
Y_test = Y['electricity'] # Dependent Variable for Test Data
decision_tree_regression(X_train, Y_train, X_test, Y_test, 200)
linear_regression(X_train, Y_train, X_test, Y_test.to_frame(), 200)
xgboost_regression(X_train.values, Y_train.values, X_test.values, Y_test, 200)
X = df1.iloc[:, 1:]
corr = np.round(X.corr(), 2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(ax=ax,
 data=corr,
 annot=True,
 cmap="coolwarm",
 vmin=-1, vmax=1, center=0)
ax.set_title("Correlation Matrix Graph")
plt.show()
cor_target = abs(corr["electricity"])