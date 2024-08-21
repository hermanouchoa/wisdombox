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

fig, axes = plt.subplots(1,2,figsize=(15,4))
sns.histplot(data=df_studio, bins=20, ax=axes[0])
axes[0].set_title("Soma do barulho dos albuns de studio")
axes[0].set_xlabel("Barulho")
axes[0].set_ylabel("Frequência")

sns.histplot(data=df_ao_vivo, bins=20, ax=axes[1])
axes[1].set_title("Soma do barulho dos albuns ao vivo")
axes[1].set_xlabel("Barulho")
axes[1].set_ylabel("Frequência")

fig.tight_layout()

plt.show()
