# pip install pandas
import pandas as pd
import os

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

path_dados = os.getenv('PATH_DADOS_ML')
print("Path Dados: "+path_dados)

#carregando xls
df_excel = pd.read_excel(path_dados+"\\Chess.xlsx", sheet_name="Chess")
print(df_excel.head())
print(df_excel.info())

#carregando csv
df_csv = pd.read_csv(path_dados+"\\Tomato.csv", sep=",")
print(df_csv.head())
print(df_csv.tail())
print(df_csv.shape)
print(df_csv.info())

print(df_csv.describe())