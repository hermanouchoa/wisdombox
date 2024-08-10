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

#para obter as categorias de uma determinada coluna
print(set(df_excel["victory_status"]))

#carregando csv
df_csv = pd.read_csv(path_dados+"\\Tomato.csv", sep=",")
print(df_csv.describe().T)

print(df_csv.head())

def categorizar_tomate_media(media):
    if media >= 40 and media <= 70:
        return "tomate medio"
    elif media < 40:
        return "tomate pequeno"
    else: 
        return "tomate grande"

df_csv["categoria_tomate"] = df_csv["Average"].apply(categorizar_tomate_media)
print(df_csv.head())

categorias = df_csv.groupby(["categoria_tomate"]).describe()
print(categorias)


print("filtrando apenas os que tem média abaixo de 40")
filtro = df_csv["Average"] < 40
print(df_csv.loc[filtro])
