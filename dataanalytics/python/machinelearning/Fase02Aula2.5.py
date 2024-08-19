# pip install pandas
# pip install numpy
# pip install matplotlib
import os
import pandas as pd

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

DADOS_PATH = os.getenv('PATH_DADOS_ML')+"\\dataset_rolling_stones.xlsx"

df = pd.read_excel(DADOS_PATH)

# criando nova coluna com duração da música em minutos
df["duracao_em_min"] = df["duration_ms"] / 60000

# agrupamento de dados
df_agrupado_por_album = df.groupby("album") #agrupando dados por album

import matplotlib.pyplot as plt

df_ultima_decada = df[df["release_date"].between(pd.to_datetime("2011"),pd.to_datetime("2020"))]
print("Última decada")
print(df_ultima_decada.head())

df_por_album = df_ultima_decada.groupby("album")["popularity"].sum().sort_values(ascending=False).head(10)
print("df_por_album")
print(df_por_album)

total_popularidade = df_por_album.sum()
print("total_popularidade")
print(total_popularidade)
df_porcetangem = (df_por_album / total_popularidade)*100
print("df_porcetangem")
print(df_porcetangem)

labels = df_porcetangem.index.tolist()
print("labels")
print(labels)

sizes = df_porcetangem.values.tolist()
print("sizes")
print(sizes)

figura, grafico = plt.subplots(figsize=(18,6))
grafico.pie(sizes, autopct="%1.1f%%")
grafico.axis('equal')
plt.title("Porcentagem de popularidade de albuns na úlitma decada (Top 10 albuns)")
plt.legend(labels, loc="best")
plt.show()
