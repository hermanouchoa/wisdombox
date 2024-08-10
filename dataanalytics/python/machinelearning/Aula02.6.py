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

plt.bar(
    df_chess[""]
)

#parei aos 15 minutos da aula