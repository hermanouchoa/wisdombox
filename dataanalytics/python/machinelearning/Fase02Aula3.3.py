import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from dotenv import load_dotenv # pip install python-dotenv
# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()
DADOS_PATH = os.getenv('PATH_DADOS_ML')+"\\data_imoveis.csv"
print("path dados "+DADOS_PATH)

dados = pd.read_csv(DADOS_PATH, sep=",")
print("head dos dados:")
print(dados.head())

# analise de relação entre "sqft_living" e "bathrooms"
x = dados[["sqft_living", "bathrooms"]].values
y = dados["price"].values

# Padronização
scaler = StandardScaler()
x_std = scaler.fit_transform(x)

x_std = pd.DataFrame(
    x_std,
    columns=["sqft_living", "bathrooms"]
    )
x_std.sqft_living.hist()
x_std.bathrooms.hist()
plt.show()

from sklearn.model_selection import train_test_split                           # Metodologia de separação dos dados
from sklearn.linear_model import LinearRegression                              # Regressão Linear
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  # Métricas de desempenho

x= dados[['sqft_living','bathrooms']].values
y = dados["price"].values

x_train, x_test, y_train, y_test = train_test_split(x,y, random_state=7)
print(len(x_train))
print(len(x_test))

scaler = MinMaxScaler()
scaler.fit(x_train)

x_train_scaled = scaler.transform(x_train)
x_test_scaled  = scaler.transform(x_test)

model = LinearRegression()

model.fit(x_train_scaled, y_train)


y_pred = model.predict(x_test_scaled)

MAE = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE: ", MAE)
print("R2: ", r2)

model_normal = LinearRegression()
model_normal.fit(x_train, y_train)

y_pred_normal = model_normal.predict(x_test)

MAE = mean_absolute_error(y_test, y_pred_normal)
r2 = r2_score(y_test, y_pred_normal)

print("MAE: ", MAE)
print("R2: ", r2)