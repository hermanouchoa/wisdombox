# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Definindo o caminho dos dados
path_dados = os.getenv('PATH_DADOS_MA')
print("Path Dados: " + path_dados)

# Carregando os dados do Excel
df_csv = pd.read_excel(path_dados + "\\Recrutamento.xlsx")
dados = df_csv

# Tratando valores nulos na coluna 'salary'
print("Tratando valores nulos em 'salary'")
dados["salary"].fillna(value=0, inplace=True)

# Selecionando apenas colunas numéricas
dados_numericos = dados.select_dtypes(include=['float64', 'int64'])

# Calculando a matriz de correlação
correlation_matrix = dados_numericos.corr().round(2)

# Plotando a matriz de correlação
#fig, ax = plt.subplots(figsize=(8, 8))
#sb.heatmap(data=correlation_matrix, annot=True, linewidths=.5, ax=ax)
#plt.show()


from sklearn.preprocessing import LabelEncoder
print( dados.head() )

colunas=['gender','workex','specialisation','status']

label_encoder = LabelEncoder()
for col in colunas:
    dados[col] = label_encoder.fit_transform(dados[col])
print( dados.head() ) 

dummy_hsc_s=pd.get_dummies(dados['hsc_s'], prefix='dummy')
dummy_degree_t=pd.get_dummies(dados['degree_t'], prefix='dummy')

dados_coeded = pd.concat([dados,dummy_hsc_s,dummy_degree_t],axis=1)
dados_coeded.drop(['hsc_s','degree_t','salary'],axis=1, inplace=True)
print( dados_coeded.head() )


x = dados_coeded[['ssc_p', 'hsc_p', 'degree_p', 'workex', 'mba_p']] #variaveis independentes
y = dados_coeded['status'] #target

print(x.head())
print(y.head())

from sklearn.model_selection import train_test_split #separação em treino e teste
from sklearn.neighbors import KNeighborsClassifier   #knn

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, stratify=y, random_state=7) 

print("x_train.shape")
print( x_train.shape )

print("x_test.shape")
print( x_test.shape )

from sklearn.preprocessing import StandardScaler, MinMaxScaler  
scaler = StandardScaler() 
#scaler = MinMaxScaler() 

scaler.fit(x_train)

x_train_escalonado = scaler.transform(x_train)
x_test_escalonado = scaler.transform(x_test)

import numpy as np

error = []

# Calculating error for K values between 1 and 10
for i in range(1, 10): #range de tentativas para k
    knn = KNeighborsClassifier(n_neighbors=i)# aqui definimos  o k
    knn.fit(x_train_escalonado, y_train) #treinando o algoritmo para encontrar o erro
    pred_i = knn.predict(x_test_escalonado) #armazenando as previsões
    error.append(np.mean(pred_i != y_test)) #armazenando o valor do erro médio na lista de erros

plt.figure(figsize=(12, 6))
plt.plot(range(1, 10), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.show()


modelo_classificador = KNeighborsClassifier(n_neighbors=5)

modelo_classificador.fit(x_train_escalonado, y_train) 

y_predito = modelo_classificador.predict(x_test_escalonado) 

print("y_predito")
print(y_predito)

from sklearn.metrics import accuracy_score 
# Metricas de precisão, revocação, f1-score e acurácia.
print("accuracy_score KNN")
print(accuracy_score(y_test, y_predito)) #relatório de validação das métrica de desempenho.

from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

svm = Pipeline([
    ("linear_svc", LinearSVC(C=1))
])

svm.fit(x_train_escalonado, y_train)
y_predito_svm = svm.predict(x_test_escalonado) 
print("accuracy_score SVM")
print(accuracy_score(y_test, y_predito_svm)) 

