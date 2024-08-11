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

from sklearn.model_selection import train_test_split

x = df_diabetes.drop(["Class variable"], axis=1)
print(x.head())

y = df_diabetes["Class variable"]
print(y.head())