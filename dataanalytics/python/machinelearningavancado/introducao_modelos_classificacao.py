# importanto as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carrega as variáveis do arquivo .env para o ambiente
import os
from dotenv import load_dotenv # pip install python-dotenv
load_dotenv()

path_dados = os.getenv('PATH_DADOS_MA')
print("Path Dados: "+path_dados)

df_csv = pd.read_excel(path_dados+"\\gaf_esp.xlsx")
dados = df_csv

print("Head")
print(
    dados.head()
)

print("Descrição dos dados")
print( 
    dados.groupby("Espécie").describe() 
)


dados.plot.scatter(x='Comprimento do Abdômen', y='Comprimento das Antenas')
#plt.show()

# separando dados de testes e de treino
#pip install -U scikit-learn
from sklearn.model_selection import train_test_split

x = dados[['Comprimento do Abdômen', 'Comprimento das Antenas']]  # variáveis caracteristicas
y = dados['Espécie'] # variável target

x_train, x_test, y_train, y_test = train_test_split(
                                                x, 
                                                y, 
                                                test_size=0.2,  # tamanho da base de testes (20% nesse caso) 
                                                stratify=y,
                                                random_state=42
                                                )

print( list(y_train).count('Gafanhoto') )
print( list(y_train).count('Esperança') )

print("Total base de treino: ", len(x_train))
print("Total base de teste: ", len(y_test))
