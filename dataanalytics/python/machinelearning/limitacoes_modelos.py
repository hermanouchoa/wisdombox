# Importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carrega as variáveis do arquivo .env para o ambiente
import os
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

path_dados = os.getenv('PATH_DADOS_ML')
print("Path Dados: "+path_dados)

df_csv = pd.read_csv(path_dados+"\\airlines.csv", sep=",")
df = df_csv

# Analisando as primeiras linhas
print(df.head(3))

# Alisando linhas e colunas
print(df.shape)

print("Analisando a consistência dos dados")
# Analisando valores nulos
df.isnull().sum()

# Limapndo dados nulos:
df = df.dropna()

duplicated_cols = []
for col in df.columns:
    if df[col].duplicated().any():
        duplicated_cols.append(col)
print(duplicated_cols)

print("Análise exploratória dos dados")
print(df.describe())

#Podemos também mesclar os dois tipos de gráficos para entender nossos valores discrepantes
fig, ax = plt.subplots(figsize=(8,6))
#Configurando o violin plot primeiramente
sns.violinplot(x='Length', data=df, ax=ax, color='lightgray')
#Por baixo vamos criar um boxplot
sns.boxplot(x='Length', data=df, ax=ax, whis=1.5, color='darkblue')
ax.set_title('Visualização Box Plot e Violin Plot')
#Mostrando o gráfico
plt.show()

sns.violinplot(x='Class', y='Length', data=df)
plt.show()


atraso_voo = df.groupby('Class')
print(atraso_voo.describe().T)

sns.violinplot(x='Class', y='Time', data=df)
plt.show()

sns.countplot(x='Airline', hue='Class', data=df)
plt.show()

diaSemana = list(range(1,8))
sns.countplot(x='DayOfWeek',data=df,order=diaSemana)
plt.show()

sns.countplot(x='Class',data=df)

print("Pré-processamento da base")
from sklearn.preprocessing import LabelEncoder
df['AirportFrom']=LabelEncoder().fit_transform(df['AirportFrom'])
df['AirportTo']=LabelEncoder().fit_transform(df['AirportTo'])

df['Airline']=LabelEncoder().fit_transform(df['Airline'])

print(df.head(3))

print("Separando a base de dados")
