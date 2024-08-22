# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install openpyxl
import os
import pandas as pd

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

DADOS_PATH = os.getenv('PATH_DADOS_ML')+"\\dataset_rolling_stones.xlsx"
df = pd.read_excel(DADOS_PATH)
# criando nova coluna com duração da música em minutos
df["duracao_em_min"] = df["duration_ms"] / 60000

def classificacao_musica_ao_vivo(df):
    if df["liveness"] >= 0.8:
        return True
    else:
        return False
    
df["ao_vivo"] = df.apply(classificacao_musica_ao_vivo, axis=1)

print("data frame com nova coluna de ao_vivo")
print(df.head())

print(df.groupby("ao_vivo")["ao_vivo"].count())

df_gravado_em_studio = df[df["ao_vivo"]==False]
df_show_ao_vivo = df[df["ao_vivo"]==True]

df_studio = df_gravado_em_studio.groupby("album")["loudness"].sum()
df_ao_vivo = df_show_ao_vivo.groupby("album")["loudness"].sum()

import matplotlib.pyplot as plt
import seaborn as sns

media_por_algum = df.groupby("album")["valence"].mean().reset_index()
media_por_album = media_por_algum.rename(columns={"valence": "media_valence"})
media_por_album["sentimento"] = [ "positivo" if v > 0.6 else "negativo" for v in media_por_album["media_valence"] ]

print(media_por_album.groupby("sentimento")["sentimento"].count())

# matriz de correlação
print(media_por_album.head())

df_resultado_final = pd.merge(df, media_por_album, on="album")
print(df_resultado_final.head())