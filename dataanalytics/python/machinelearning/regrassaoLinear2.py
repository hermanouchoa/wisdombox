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
# plt.hist(imoveis['Valor'], bins=5)
# plt.ylabel('Frequência')
# plt.xlabel('Valor')
# plt.title('Histograma Valor')
# plt.show()

# aula 2
imoveis['raiz_valor'] = np.sqrt(imoveis['Valor'])
print(imoveis.head())

# Histograma da variável target 
plt.hist(imoveis['raiz_valor'], bins=5)
plt.ylabel('Frequência')
plt.xlabel('Valor')
plt.title('Histograma raiz_valor')

# Avaliando as variáveis quantitativas Boxplot: para visualizar Outliers

plt.figure(figsize=(24,20))

plt.subplot(4, 2, 1)
fig = imoveis.boxplot(column='Valor')
fig.set_title('')
fig.set_ylabel('Valor em 100R$')


plt.subplot(4, 2, 2)
fig = imoveis.boxplot(column='Area')
fig.set_title('')
fig.set_ylabel('Area em M2')


plt.subplot(4, 2, 3)
fig = imoveis.boxplot(column='IA')
fig.set_title('')
fig.set_ylabel('IA')

plt.subplot(4, 2, 4)
fig = imoveis.boxplot(column='Andar')
fig.set_title('')
fig.set_ylabel('Andar')

plt.subplot(4, 2, 5)
fig = imoveis.boxplot(column='DistBM')
fig.set_title('')
fig.set_ylabel('DistBM')

plt.subplot(4, 2, 6)
fig = imoveis.boxplot(column='Suites')
fig.set_title('')
fig.set_ylabel('Suites')


correlation_matrix = imoveis.corr().round(2)
fig, ax = plt.subplots(figsize=(8,8))    
sb.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
plt.show()