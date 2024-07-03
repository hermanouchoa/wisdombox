#pip install pandas
#pip install matplotlib

import pandas as pd

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

