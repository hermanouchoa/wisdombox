# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install scikit-learn
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from DataFrameDiabetes import DataFrameDiabetes
df_diabetes = DataFrameDiabetes()
df_diabetes = df_diabetes.to_dataframe()
print(df_diabetes.head())

# Dividindo bases de treinamento (x) e teste (y)

from sklearn.model_selection import train_test_split
x = df_diabetes.drop(["Class variable"], axis=1)
print(x.head())

y = df_diabetes["Class variable"]
print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

print("x_train")
print(x_train.head())

# Definindo modelo de ML
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

accuracy = knn.score(x_test, y_test)
print(accuracy)
