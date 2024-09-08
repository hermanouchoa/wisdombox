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

# #Podemos também mesclar os dois tipos de gráficos para entender nossos valores discrepantes
# fig, ax = plt.subplots(figsize=(8,6))
# #Configurando o violin plot primeiramente
# sns.violinplot(x='Length', data=df, ax=ax, color='lightgray')
# #Por baixo vamos criar um boxplot
# sns.boxplot(x='Length', data=df, ax=ax, whis=1.5, color='darkblue')
# ax.set_title('Visualização Box Plot e Violin Plot')
# #Mostrando o gráfico
# plt.show()

# sns.violinplot(x='Class', y='Length', data=df)
# plt.show()


atraso_voo = df.groupby('Class')
# print(atraso_voo.describe().T)

# sns.violinplot(x='Class', y='Time', data=df)
# plt.show()

# sns.countplot(x='Airline', hue='Class', data=df)
# plt.show()

diaSemana = list(range(1,8))
# sns.countplot(x='DayOfWeek',data=df,order=diaSemana)
# plt.show()

sns.countplot(x='Class',data=df)

print("Pré-processamento da base")
from sklearn.preprocessing import LabelEncoder
df['AirportFrom']=LabelEncoder().fit_transform(df['AirportFrom'])
df['AirportTo']=LabelEncoder().fit_transform(df['AirportTo'])

df['Airline']=LabelEncoder().fit_transform(df['Airline'])

print(df.head(3))

print("Separando a base de dados")
from sklearn.model_selection import train_test_split

x = df[['Flight', 'Time',  'Length', 'Airline', 'AirportFrom', 'AirportTo', 'DayOfWeek']]
y = df['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=7)

print("Criando o modelo de naive bayes")
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
gnb.fit(x_train, y_train)

# Predizendo valores
y_pred = gnb.predict(x_test)

print("Validando o modelo")
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy,2))

print("Equilibrando a base de dados")
from sklearn.utils import resample

# Separando as classes majoritárias e minoritárias
df_majority = df[df.Class == 0]
df_minority = df[df.Class == 1]

# Upsampling da classe minoritária
df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority),  random_state=7)

# Juntando os dois DataFrames
df_equilibrado = pd.concat([df_majority, df_minority_upsampled])
sns.countplot(x='Class',data=df_equilibrado)
plt.show()

print("Testando o algoritmo com a base equilibrada")
x_equilibrado = df_equilibrado[['Flight', 'Time', 'Length',  'DayOfWeek']]
y_equilibrado = df_equilibrado['Class']

x_train, x_test, y_train, y_test = train_test_split(x_equilibrado, y_equilibrado, test_size=0.3, stratify=y_equilibrado , random_state=7)

# Treinando o algoritmo
gnb_equilibrado = GaussianNB()
gnb_equilibrado.fit(x_train, y_train)

# Predizendo valores
y_pred_gnb_equilibrado = gnb_equilibrado.predict(x_test)

print("Validando o modelo")
accuracy_equilibrado = accuracy_score(y_test, y_pred_gnb_equilibrado)
print("Accuracy:", round(accuracy_equilibrado,2))

print("Testando com Random Forest")
from sklearn.ensemble import RandomForestClassifier
x_train, x_test, y_train, y_test = train_test_split(x_equilibrado, y_equilibrado, test_size=0.3, random_state=7)

# Instancia o modelo Random Forest e define os hiperparâmetros
rf = RandomForestClassifier( random_state=7)

# Treina o modelo com o conjunto de treinamento
rf.fit(x_train, y_train)

# Faz previsões no conjunto de teste
y_pred_rf = rf.predict(x_test)

print("Validando o modelo")
accuracy_equilibrado_rf = accuracy_score(y_test, y_pred_rf)
print("Accuracy:", round(accuracy_equilibrado_rf,2))