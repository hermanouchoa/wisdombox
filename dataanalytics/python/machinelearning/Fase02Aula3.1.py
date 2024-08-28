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

# correção de dados
correlation_matrix = dados.corr(numeric_only=True).round(2)
print("correlação")
print(correlation_matrix)

fig, ax = plt.subplots(
    figsize=(8,8)
)
sns.heatmap(
    data=correlation_matrix,
    annot=True,
    linewidths=.5,
    ax=ax
)
plt.show()

# analise de relação entre "sqft_living" e "bathrooms"
x = dados[["sqft_living", "bathrooms"]].values
y = dados["price"].values

sns.scatterplot(
    data=dados,
    x="bathrooms",
    y="price"
)
plt.show()

fig, ax = plt.subplots(
    figsize=(12,4)
)
ax.scatter(
    x[:,0],
    y
)
ax.scatter(
    x[:,1],
    y
)
plt.show()

sns.histplot(
    data=dados,
    x="sqft_living",
    kde=True
)
plt.show()
