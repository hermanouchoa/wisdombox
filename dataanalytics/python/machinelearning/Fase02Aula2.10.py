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

plt.figure(figsize=(10,5))
sns.kdeplot(
    data=df_studio, 
    label="Albuns de Studio",
    fill=True
)
sns.kdeplot(
    data=df_ao_vivo, 
    label="Albuns Ao Vivo",
    fill=True
)

plt.title("Distribuição do barulho dos albuns")
plt.xlabel("Barulho")
plt.ylabel("Densidade")
plt.legend()
plt.show()


from scipy.stats import shapiro

stat, p = shapiro(df_studio)
print("Soma do Barulho dos Albuns de Studio: ")
print("Estatistica de Teste: {:.4f}, valor p: {}".format(stat,p))

if p > 0.05:
    print("Não há evidencia suficiente para rejeitar a hipotese de normalidade")
else:
    print("A hipotese de normalidade é rejeitada")

stat, p = shapiro(df_ao_vivo)
print("Soma do Barulho dos Albuns Ao Vivo: ")
print("Estatistica de Teste: {:.4f}, valor p: {}".format(stat,p))

if p > 0.05:
    print("Não há evidencia suficiente para rejeitar a hipotese de normalidade")
else:
    print("A hipotese de normalidade é rejeitada")


from scipy.stats import mannwhitneyu

stat, p = mannwhitneyu(
    df_studio.sample( len(df_studio) ), 
    df_ao_vivo.sample( len(df_ao_vivo) ),
    alternative="less"
    )

print("Estatistica de teste U: ", stat)
print("Valor p: ", p)

alpha = 0.05
if p < alpha:
    print("Diferença estatisticamento significante")
else:
    print("Não há diferença estatisticamente significante")