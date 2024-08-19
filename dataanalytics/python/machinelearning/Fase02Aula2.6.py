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

df_por_album = df_ultima_decada.groupby("album")["popularity"].sum().sort_values(ascending=False).head(10)

total_popularidade = df_por_album.sum()
df_porcetangem = (df_por_album / total_popularidade)*100

labels = df_porcetangem.index.tolist()
sizes = df_porcetangem.values.tolist()

import seaborn as sns

# criando boxplot para identificar outliers
sns.set(style="whitegrid")
fig, axes = plt.subplots(figsize=(12,6))
sns.boxplot(
    x="duracao_em_min",
    data=df    
)
axes.set_title("Boxplot")
plt.show()

# criando violinplot
fig, axes = plt.subplots(figsize=(12,6))
sns.violinplot(x="duracao_em_min", data=df, color="gray")
axes.set_title("Gráfico de Violino")
plt.show()

# criando gráfico de violino e boxplot juntos
fig, ax = plt.subplots(figsize=(8,6))
sns.violinplot(
    x="duracao_em_min", data=df, 
    ax=ax, color="lightgray"
    )
sns.boxplot(
    x="duracao_em_min",
    data=df,
    ax=ax,
    whis=1.5,
    color="darkblue"
)
ax.set_title("Visuação violino e boxplot juntos")
#axes.set_title("Gráfico de Violino ")
plt.show()