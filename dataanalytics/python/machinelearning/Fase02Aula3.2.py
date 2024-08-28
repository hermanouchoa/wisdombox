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