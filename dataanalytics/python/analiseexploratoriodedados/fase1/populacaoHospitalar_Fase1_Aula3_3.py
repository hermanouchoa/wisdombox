#pip install pandas
#pip install matplotlib

# FASE 1 | AULA 3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

pathArquivoDeDados = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_processamento.csv'

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
print("Colunas Usaveis")
print(colunasUsaveis[:5])

print("Dados Usaveis - Colunas Usaveis")
dadoUsaveis = dados[colunasUsaveis] # o conjunto da dados agora será apenas sobre as colunas com dados válidos
print(dadoUsaveis.head())

print("Dados Usaveis com novo indice, Unidade da Federação")
dadoUsaveis = dadoUsaveis.set_index("Unidade da Federação") # alterando o indece do dataframe
print(dadoUsaveis.head())

np.random.seed(524387)
dadoUsaveis = dadoUsaveis.sample(n=7)

print("Dados usuaveis - amostra randomica")
print(dadoUsaveis.head())

print("Dados usuaveis - Adicionada coluna de Total")
dadoUsaveis["Total"] = dadoUsaveis.sum(axis=1) #adicionando no final uma coluna de total
print(dadoUsaveis.head())

print("Ordenação")
ordenadosPorTotal = dadoUsaveis.sort_values(by="Total", ascending=False)
ordenadosPorTotal = ordenadosPorTotal.drop("Total", axis=1)
print(ordenadosPorTotal.head(5))

print("Colunas interessadas")
colunasInteressadas = ordenadosPorTotal.columns[0:]
print(colunasInteressadas)

ordenadosPorTotal = ordenadosPorTotal[colunasInteressadas]

ordenadosPorTotal.head(5).T.plot(figsize=(10,6))

plt.show()

### Desafio
###     Adicionar seu estado aos 5 estados existenes, e plotar
###     Deixar o gráfico mais refinado
###     Pesquisar os casos de dengue do Brasil e verificar se existe algum padrão com os gastos encontrados aqui!
###     Plotar estados de somente uma regiao do Brasil