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
print("Gerando média dos dados")
media = dados.mean(numeric_only=True)
print(media)

print("--------------------")
print("Tratamento de Colunas - Colunas Usaveis")
colunasUsaveis = media.index.to_list() # gerando uma lista do python a partir do index da média. (o index da média é o nome das colunas do conjunto de dados)
print(colunasUsaveis)

print("--------------------")
print("Tratamento de Colunas - Colunas Usaveis (inserindo coluna de UF)")
colunasUsaveis.insert(0,"Unidade da Federação") # inserindo em uma lista do python mais um registro no inicio da lista
colunasUsaveis[:5]
print(colunasUsaveis)

print("--------------------")
print("Dados Usaveis")
dadosUsaveis = dados[colunasUsaveis]
headDadosUsaveis = dadosUsaveis.head()
print(headDadosUsaveis)

print("--------------------")
print("Dados Usaveis - Mudando indice do cojunto de dados")
dadosUsaveis = dados[colunasUsaveis]
dadosUsaveis = dadosUsaveis.set_index("Unidade da Federação")
print(dadosUsaveis)

print("Dados Usaveis (head) - Indice do cojunto de dados alterado")
headNovoDadosUsaveis = dadosUsaveis.head()
print(headNovoDadosUsaveis)

print("--------------------")
print("Localizando pelo indice. Dados do Ceará")
dadsoCeara = dadosUsaveis.loc["23 Ceará"]
print(dadsoCeara)


print("--------------------")
print("Dados Gráfico")
#removendo a linha de total do conjunto de dados que será utilizado para o gráfico
dadosGrafico = dadosUsaveis.drop(
    "Total" # desejo remover a linha com o indice "Total"
    ,axis=1 # definindo o eixo que será realizado do drop (0 (zero) = procura nas linhas / 1 (um) = produta nas colunas)
    )
#dadosGrafico = dadosGrafico[:7] #sete primeiras linhas

import numpy as np
np.random.seed(1234) 

dadosGrafico = dadosGrafico.sample(n=7) #obter sete registros randomicamente dentro do dataframe
dadosGrafico = dadosGrafico.T # para transpor das colunas (transforma linhas em colunas e colunas em linhas)

print("--------------------")
print("Criando Grafico - Linhas Temporal")
import matplotlib.ticker as ticker
axis = dadosGrafico.plot(
    #x="Unidade da Federação" # eixa 'x'
    #,y="2008/Ago" # eixo 'y'
    #,kind="bar" # tipo de gráfico (barras)
    figsize=(10,6) # tamanho do grário (horizontal,vertical)
     )
axis.yaxis.set_major_formatter( ticker.StrMethodFormatter("{x:,.2f}") ) # mudando o formatador no eixo 'Y'
#plt.title("Valor por Unidade da Federação (UF)") # mudando título do gráfico
#plt.show()


print("--------------------")
print("Adicionando Coluna de Total")
dadosGrafico["Total"] = dadosGrafico.sum(
    axis=1 # eixa 'x' para adicionar uma nova coluna
)
print(dadosGrafico.head())

print("--------------------")
print("Ordenando")
ordenadosPorTotal = dadosGrafico.sort_values(by="Total")
ordenadosPorTotal = ordenadosPorTotal.drop("Total", axis=1)
print(ordenadosPorTotal.head())

print("Ordenando decrescente")
ordenadosPorTotalDesc= dadosGrafico.sort_values(by="Total", ascending=False)
print(ordenadosPorTotalDesc.head())

dadosGrafico = ordenadosPorTotal.drop("Total", axis=1)
dadosGrafico.head(5).T.plot(figsize=(10,6), title="A")
plt.show()

# Desafio
#   Adicionar seu estado aos cinco estados existentes
#   Deixa o gráfico mais refinado (gráficos, labels, etc)
#   Pesquisar o sort_index
#   Procurar os casos de dengue do Brasil e verificar se existe algum padrão com os gastos encontrados aqui
#   Plotar somente os estados de uma região do Brasil