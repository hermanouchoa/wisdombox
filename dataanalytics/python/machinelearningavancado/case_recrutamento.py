# importanto as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carrega as variáveis do arquivo .env para o ambiente
import os
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

path_dados = os.getenv('PATH_DADOS_MA')
print("Path Dados: "+path_dados)

df_csv = pd.read_excel(path_dados+"\\Recrutamento.xlsx")
dados = df_csv

print("Head dos Dados")
print(
    dados.head()
)

print("Analisando variavel")
print(set(dados.status))

print("Descrição dos dados")
print( 
    dados.describe() 
)
print("Descrição dos dados - por specialisation")
print( 
    dados.groupby("specialisation").describe() 
)

print("Verificando dados 'nulos' no conjunto de dados")
import missingno as msno # pip install missingno
msno.matrix(dados)
plt.show()

print(
    dados.isnull().sum() 
)

import seaborn as sb
sb.boxplot(x='status', y='salary', data=dados, palette='hls')
plt.show()

print("Tratando valores nulos em 'salary'")
dados["salary"].fillna(value=0, inplace=True) # Preenche/altera os dados nulos para 0 (zero)
print(
    dados.isnull().sum() 
)

sb.boxplot(x=dados["salary"])
plt.show()

sb.histplot(data=dados, x="salary")
plt.show()

