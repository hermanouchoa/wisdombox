#pip install pandas
#pip install matplotlib

# FASE 1 | AULA 4

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

#pathArquivoDeDados = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_processamento.csv'
pathArquivoDeDados = 'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_processamento.csv'

#criando um dataframe
dados = pd.read_csv(
     pathArquivoDeDados     
    , encoding='ISO-8859-1'
    , skiprows=3 # para não ler as primeiras linhas
    , sep=';' # para definir o caractere de separação do arquivo csv
    , skipfooter=12 # para não ler as úlitmas linhas
    , thousands='.' # para separação da milhar
    , decimal=',' # para separação de decimal
    , engine='python'
    )

# Com a média estarei obtendo apenas as colunas com valores válidos, visto que não é possível ober média das colunas com valores vários.
media = dados.mean(numeric_only=True) # Utilizando o mean para obter a média. 
colunasUsaveis = media.index.to_list()
colunasUsaveis.insert(0, "Unidade da Federação") #inserindo mais um item na lista python
#print("Colunas Usaveis")
#print(colunasUsaveis[:5])

#print("Dados Usaveis - Colunas Usaveis")
dadoUsaveis = dados[colunasUsaveis] # o conjunto da dados agora será apenas sobre as colunas com dados válidos
#print(dadoUsaveis.head())

#print("Dados Usaveis com novo indice, Unidade da Federação")
dadoUsaveis = dadoUsaveis.set_index("Unidade da Federação") # alterando o indece do dataframe
#print(dadoUsaveis.head())

np.random.seed(524387)
#dadoUsaveis = dadoUsaveis.sample(n=7)

#print("Dados usuaveis - amostra randomica")
#print(dadoUsaveis.head())

#print("Dados usuaveis - Adicionada coluna de Total")
dadoUsaveis["Total"] = dadoUsaveis.sum(axis=1) #adicionando no final uma coluna de total
#print(dadoUsaveis.head())

#print("Ordenação")
ordenadosPorTotal = dadoUsaveis.sort_values(by="Total", ascending=False)
ordenadosPorTotal = ordenadosPorTotal.drop("Total", axis=1)
#print(ordenadosPorTotal.head(5))

print("Colunas interessadas")
colunasInteressadas = ordenadosPorTotal.columns[-60:]
#print(colunasInteressadas)

ordenadosPorTotal = ordenadosPorTotal / 1000000 
ordenadosPorTotal = ordenadosPorTotal[colunasInteressadas]
#print(ordenadosPorTotal.head())

mesMaisRecente = ordenadosPorTotal.columns[-1]
print("Mes mais recente: ")
print(mesMaisRecente)

gastosMaisRecente = ordenadosPorTotal[mesMaisRecente]
print(gastosMaisRecente)

tabelaDeComparacao = gastosMaisRecente / gastosMaisRecente.loc["23 Ceará"]
print("Tabela de Comparação")
print(tabelaDeComparacao.head())

tabelaDeComparacao = tabelaDeComparacao.sort_values(ascending=False)

tabelaDeComparacao.plot(kind='bar')

plt.show()

### Desafio
###     Atualizar o último gráfico para refletir o seu estado, incluindo grid, eixos, etc
###     Colorir o seu estado com um tom diferente. Escolher dois estados, plotar a comparação desses gastos de acordo com a população deles.
###            (base IBGE por exemplo)
###     Passar uma linha horizontal no seu estado
###     Explore gráficos e as tabelas, encontrole o que você acha de interessante, levante perguntas e hipóteses
###     Escolha outro valor além de "Valor Aprovado" no Tabnet