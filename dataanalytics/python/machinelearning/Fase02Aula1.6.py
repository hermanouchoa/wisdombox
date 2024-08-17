# pip install pandas
# pip install numpy
# pip install matplotlib
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

path_dados = os.getenv('PATH_DADOS_ML')
print("Path Dados: "+path_dados)

#carregando xls de chess
df_chess = pd.read_excel(path_dados+"\\Chess.xlsx", sheet_name="Chess")

print(df_chess)
print(df_chess.info())

plt.scatter(
    df_chess["black_rating"],
    df_chess["white_rating"],
)
plt.xlabel("Black")
plt.ylabel("White")
plt.title("Partidas de peças pretas x peças brancas")

plt.show()

#-------------------------------------------------------------------
#gráfico em barras

#carregando csv de tomatos
df_tomato = pd.read_csv(path_dados+"\\Tomato.csv", sep=",")
#print(df_tomato.describe().T)
#print(df_tomato.head())

def categorizar_tomate_media(media):
    if media >= 40 and media <= 70:
        return "tomate medio"
    elif media < 40:
        return "tomate pequeno"
    else: 
        return "tomate grande"

df_tomato["categoria_tomate"] = df_tomato["Average"].apply(categorizar_tomate_media)
#print(df_tomato.head())
print(df_tomato.info())

#convertendo coluna "Date" para datetime
df_tomato["Date"] = pd.to_datetime(df_tomato["Date"])
print(df_tomato.info())

plt.bar(
    df_tomato["categoria_tomate"], #eixo "x"
    df_tomato["Average"], #eixo "y"    
)

plt.xlabel("Categoria Tomates") #rotulando o eixo "x"
plt.ylabel("Média em Kg de Tomates") #rotulando o eixo "y"
plt.title("Média de tomates por categoria") #titulo do gráfico

plt.show()

