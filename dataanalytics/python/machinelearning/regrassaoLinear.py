# importanto as bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats

# Carrega as variáveis do arquivo .env para o ambiente
import os
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

path_dados = os.getenv('PATH_DADOS_ML')
print("Path Dados: "+path_dados)

df_csv = pd.read_csv(path_dados+"\\Valorizacao_Ambiental.csv", sep=";")
imoveis = df_csv

print(imoveis.head())
print(imoveis.shape)

print("Verificando dados nulos")
print(imoveis.isnull().sum())

print("arredondando")
print( imoveis.describe().round(2) )

# Histograma da variável target

plt.hist(imoveis['Valor'], bins=5)
plt.ylabel('Frequência')
plt.xlabel('Valor')
plt.title('Histograma Valor')
plt.show()