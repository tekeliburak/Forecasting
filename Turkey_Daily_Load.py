import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# -------------------------------------------------------------------------
# Estimation of consumption
# -------------------------------------------------------------------------------------
read_csv = pd.read_csv('ConsumptionData.csv', parse_dates=['time']) # Read data set from csv file
read_csv_new = pd.get_dummies(read_csv, columns=['type', 'week']) # One Hot Coding
train_data = read_csv_new[0:14616] # Train Data
test_data = read_csv_new[14616:len(read_csv_new)] # Test Data
X_train = train_data[['month', 'day', 'hour', 'day_of_week', 'type_normal', 
'type_national', 'type_special',
 'type_religious', 'week_weekday', 'week_weekend']] # Independent Variables for Train Data
Y_train = train_data[['consumption']] # Dependent Variables for Train Data
X_test = test_data[['month', 'day', 'hour', 'day_of_week', 'type_normal', 
'type_national', 'type_special',
 'type_religious', 'week_weekday', 'week_weekend']] # Independent Variables for Test Data
Y_test = test_data[['consumption']] # Dependent Variables for Test Data
decision_tree_regression(X_train.values, Y_train.values, X_test.values, Y_test.values, 200)
linear_regression(X_train, Y_train, X_test, Y_test, 200)
xgboost_regression(X_train.values, Y_train.values, X_test.values, Y_test.values, 200)
# -------------------------------------------------------------------------------------
# Correlation Matrix Graph for Consumption
# -------------------------------------------------------------------------------------

X = read_csv_new.iloc[:, 1:]
corr = np.round(X.corr(), 2)
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(ax=ax,
 data=corr,
 annot=True,
 cmap="coolwarm",
 vmin=-1, vmax=1, center=0)
ax.set_title("Correlation Matrix Graph")
plt.show()
cor_target = abs(corr["consumption"])


