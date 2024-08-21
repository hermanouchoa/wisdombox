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

print("Média das músicas ao vivo: ", df_show_ao_vivo["duracao_em_min"].mean())
print("Média das músicas em studio: ", df_gravado_em_studio["duracao_em_min"].mean())