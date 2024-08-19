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
print("Tempo médico de músicas por album")
print(df_agrupado_por_album["duracao_em_min"].mean())

import matplotlib.pyplot as plt

df_maior_duracao_musica = df_agrupado_por_album["duracao_em_min"].mean().sort_values(ascending=False) # ordenação do maior para o menor
print("Tempo médio de músicas por album do maior para o menor")
print(df_maior_duracao_musica.head())

df_maior_duracao_musica.head(5).plot(kind="bar")
plt.xlabel("Alguns")
plt.ylabel("Média de duração das músicas")
plt.title("Top 5 albuns com maior duração média de músicas")
plt.show()