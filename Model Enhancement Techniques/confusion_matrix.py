# -*- coding: utf-8 -*-
"""Confusion_Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kC53QCHSCafy75vwXI-Tcg-7A9sgyAT0
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

def iris_type(row):
  if row['Target']== 0:
    return 'iris-setosa'
  elif row['Target']== 1:
    return 'iris-versicolor'
  elif row['Target']== 2:
    return 'iris-vergicolor'

iris= load_iris()
df = pd.DataFrame(iris.data)
df.columns=['Sepal_length', 'Sepal_Width', 'Petal_length', 'Petal_Width']
df['Target']=iris.target
df['Iris_Type']=df.apply(iris_type, axis=1)
class_names = iris.target_names

X = df[df.columns[0:4]].values
y = df[df.columns[5]].values

#split the data into training and testing data
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

knn_clf = KNeighborsClassifier(n_neighbors=9)
knn_clf.fit(X_train, y_train)
knn_predictions = knn_clf.predict(X_test)
print("Accuracy score of the algorithm is:", accuracy_score(y_test, knn_predictions))

confusion_matrix(y_test, knn_predictions)

# Plot non-normalized confusion matrix
titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        knn_clf,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)

    print(title)
    print(disp.confusion_matrix)

plt.show()