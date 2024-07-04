#pip install pandas
#pip install matplotlib
#python -m pip install seaborn

import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns


#criando um dataframe
dados = pd.read_csv(
     #'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_atendimento.csv'
     'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_processamento.csv'
    , encoding='ISO-8859-1'
    , skiprows=3 # para não ler as primeiras linhas
    , sep=';' # para definir o caractere de separação do arquivo csv
    , skipfooter=12 # para não ler as úlitmas linhas
    , thousands='.' # para separação da milhar
    , decimal=',' # para separação de decimal
    #, engine='python'
    )

print("--------------------")
print("Head (primeiras linhas do dataframe)")
primeirasLinhas = dados.head()
print(primeirasLinhas)

print("--------------------")
print("Tail (últimas linhas do dataframe)")
ultimasLinhas = dados.tail()
print(ultimasLinhas)

print("--------------------")
print("Info")
informacoesDataFrame = dados.info()
print(informacoesDataFrame)

# Ajustando formação dos valores
pd.options.display.float_format = '{:.2f}'.format

#gerando a média de uma coluna
print("--------------------")
print("Média Ago 2008")
mediaAgosto2008 = dados["2008/Ago"].mean()
print(mediaAgosto2008)

#exibindo informações de uma coluna
print("--------------------")
print("Média Ago 2008")
agosto2008 = dados["2008/Ago"]
print(agosto2008)

#plot da serie
print("--------------------")
print("Criando Grafico")
dados.plot(
     x="Unidade da Federação" # eixa 'x'
    ,y="2008/Ago" # eixo 'y'
    )
#plt.show()  #Descomentar para exibir o gráfico

print("--------------------")
print("Criando Grafico - Barras")
dados.plot(
     x="Unidade da Federação" # eixa 'x'
    ,y="2008/Ago" # eixo 'y'
    ,kind="bar" # tipo de gráfico (barras)
    ,figsize=(9,6) # tamanho do grário (horizontal,vertical)
     )
#plt.show() #Descomentar para exibir o gráfico

print("--------------------")
print("Criando Grafico - Barras - DESAFIO!")
import matplotlib.ticker as ticker
axis = dados.plot(
     x="Unidade da Federação" # eixa 'x'
    ,y="2008/Ago" # eixo 'y'
    ,kind="bar" # tipo de gráfico (barras)
    ,figsize=(9,6) # tamanho do grário (horizontal,vertical)
     )
axis.yaxis.set_major_formatter( ticker.StrMethodFormatter("{x:,.2f}") ) # mudando o formatador no eixo 'Y'
plt.title("Valor por Unidade da Federação (UF)") # mudando título do gráfico
plt.show()

#Desafios:
#   Executar o gráfico anterior com o mês mais recente
#   Deixar as legendas ângulares (0,45 etc) para facilitar a leitura
print("--------------------")
print("Criando Grafico - Barras (Com Formatação)")
import matplotlib.ticker as ticker
axis = dados.plot(
     x="Unidade da Federação" # eixa 'x'
    ,y="2008/Ago" # eixo 'y'
    ,kind="bar" # tipo de gráfico (barras)
    ,figsize=(9,6) # tamanho do grário (horizontal,vertical)
     )
axis.yaxis.set_major_formatter( ticker.StrMethodFormatter("{x:,.2f}") ) # mudando o formatador no eixo 'Y'
plt.title("Valor por Unidade da Federação (UF) - DESAFIO") # mudando título do gráfico

plt.xticks(rotation=45, ha='right') # DESAFIO: Deixar as legendas ângulares (0,45 etc) para facilitar a leitura

plt.show()