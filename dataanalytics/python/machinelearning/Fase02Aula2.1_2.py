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
# verificando as primeiras linhas
print("head")
print(df.head())

# verificando informações como tipo e tamanho da base
print("info")
print(df.info())

# vendo formato dos dados (linhas e colunas)
print("shape")
print(df.shape)

# data da primeira música
print("Data Inicial: ", df["release_date"].min() )

# data da última música
print("Data Final: ", df["release_date"].max() )

print("Dados nulos?")
print(df.isnull())
print(df.isnull().sum())

print("Dados duplicados?")
print(df.duplicated().sum())
print("Registros duplicados:")
print(df[df.duplicated()])