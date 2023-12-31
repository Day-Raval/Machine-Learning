# -*- coding: utf-8 -*-
"""Ridge Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zQDcE4Mz4d4rU0wG3DlMr_3xJ2VbjGJ_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading dataset
from sklearn.datasets import load_diabetes
data = load_diabetes()

print(data.DESCR)

#selecting indepedent and dependent features from the dataset
X = data.data
y = data.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

from sklearn.linear_model import LinearRegression
l = LinearRegression()

#fitting the model
l.fit(X_train,y_train)

y_pred = l.predict(X_test)

from sklearn.metrics import r2_score, mean_squared_error

print("R2-score:",r2_score(y_test,y_pred))
print("RMSE:",np.sqrt(mean_squared_error(y_test,y_pred)))

from sklearn.linear_model import Ridge
R = Ridge()

#To improve the r2-score and prevent overfitting, we use Ridge Regression
R = Ridge(alpha=0.0001)

R.fit(X_train,y_train)

r_pred = R.predict(X_test)

from sklearn.metrics import r2_score, mean_squared_error

print("R2-score:",r2_score(y_test,r_pred))
print("RMSE:",np.sqrt(mean_squared_error(y_test,r_pred)))