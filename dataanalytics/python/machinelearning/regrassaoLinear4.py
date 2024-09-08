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

imoveis['raiz_valor'] = np.sqrt(imoveis['Valor'])
print(imoveis.head())

# Regressão linear múltipla
from sklearn.linear_model import LinearRegression

#Criando o modelo de regressão linear
lr = LinearRegression()

# X contem as variáveis preditoras ou independentes
X = imoveis[['Area','Suites', 'IA', 'Semruido', 'Vista', 'Andar','AV100m','DistBM']]

# y variável target ou dependente
y = imoveis[['Valor']]

from sklearn.model_selection import train_test_split

#Separando os dados de Treino e Teste
# random_state é o número aleatório usado para sortear as amostras. O seu uso é opcional.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 101)

#Treinando o Modelo
lr.fit(X_train,y_train)

# Calculando o valor predito da variável resposta na amostra teste 
y_pred = lr.predict(X_test)

#Verificando o resultado
r_sq = lr.score(X, y)
print('Coeficiente de Determinação (R²):', r_sq)

# Primeiro, vamos olhar o Intercepto e os Coeficientes da Regressão.
print('Intercepto:', lr.intercept_)

coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(lr.coef_))], axis = 1)
coefficients

fig = plt.figure(figsize=(8, 6), dpi=80)
plt.rcParams.update({'font.size': 14})
ax = sb.regplot(x = y_test, y = y_pred)
ax.set(xlabel='y real', ylabel='y predito')
ax = plt.plot(y_test, y_test, '--r')
plt.show()

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Avaliando o modelo
MAE = mean_absolute_error(y_test, y_pred)
MSE = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('MAE',MAE) # Mean Absolute Error (MAE) é a média do valor absoluto dos erros.
print('MSE',MSE) # Erro Quadrático Médio (MSE) é a média dos erros quadráticos
print('r²',r2) # (R-quadrado)

#Avaliando com DecisionTreeRegressor
print("Avaliando com DecisionTreeRegressor")

from sklearn.tree import DecisionTreeRegressor
# Criando o modelo de DecisionTreeRegressor
model_dtr = DecisionTreeRegressor(random_state=7, max_depth=10)
model_dtr.fit(X_train, y_train)

y_pred_model_dtr = model_dtr.predict(X_test)

# Avaliando o modelo
MAE = mean_absolute_error(y_test, y_pred_model_dtr)
MSE = mean_squared_error(y_test, y_pred_model_dtr)
r2 = r2_score(y_test, y_pred_model_dtr)
print('MAE',MAE) # Mean Absolute Error (MAE) é a média do valor absoluto dos erros.
print('MSE',MSE) # Erro Quadrático Médio (MSE) é a média dos erros quadráticos
print('r²',r2) # (R-quadrado)

#Avaliando com SVR
print("Avaliando com SVR")
from sklearn.svm import SVR

# Criando o modelo de SVM
svr = SVR(kernel='linear')

svr.fit(X_train, y_train)

y_pred_svr = svr.predict(X_test)

# Avaliando o modelo
MAE = mean_absolute_error(y_test, y_pred_svr)
MSE = mean_squared_error(y_test, y_pred_svr)
r2 = r2_score(y_test, y_pred_svr)
print('MAE',MAE) # Mean Absolute Error (MAE) é a média do valor absoluto dos erros.
print('MSE',MSE) # Erro Quadrático Médio (MSE) é a média dos erros quadráticos
print('r²',r2) # (R-quadrado)