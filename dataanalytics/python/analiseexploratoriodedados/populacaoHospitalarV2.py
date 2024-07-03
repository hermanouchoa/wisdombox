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
    , engine='python'
    )

# FASE 1 - AULA 3

print("--------------------")
print("Selecionando mais de uma coluna")
colunasAgoSet = dados[
    ["2008/Ago","2008/Set"]
]
headColunasAgoSet = colunasAgoSet.head()
print(headColunasAgoSet)

print("--------------------")
print("Todas as Colunas do Dataframe")
colunas = dados.columns # obter todas as colunas do dataframe
print(colunas)

print("--------------------")
colunasUsaveis = dados.mean(numeric_only=True)
print(colunasUsaveis)










# print("--------------------")
# print("Criando Grafico - Barras (Com Formatação)")
# import matplotlib.ticker as ticker
# axis = dados.plot(
#      x="Unidade da Federação" # eixa 'x'
#     ,y="2008/Ago" # eixo 'y'
#     ,kind="bar" # tipo de gráfico (barras)
#     ,figsize=(9,6) # tamanho do grário (horizontal,vertical)
#      )
# axis.yaxis.set_major_formatter( ticker.StrMethodFormatter("{x:,.2f}") ) # mudando o formatador no eixo 'Y'
# plt.title("Valor por Unidade da Federação (UF)") # mudando título do gráfico
# plt.show()

