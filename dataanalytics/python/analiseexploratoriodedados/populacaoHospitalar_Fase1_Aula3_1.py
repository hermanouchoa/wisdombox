#pip install pandas
#pip install matplotlib

# FASE 1 | AULA 3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

#selecionando "n" colunas
print("Selecionando 'n' colunas")
nColunas = dados[ ["2008/Ago","2008/Set"] ]
print(nColunas.head())


# Com a média estarei obtendo apenas as colunas com valores válidos, visto que não é possível ober média das colunas com valores vários.
media = dados.mean(numeric_only=True) # Utilizando o mean para obter a média. 
colunasUsaveis = media.index.to_list()
colunasUsaveis.insert(0, "Unidade da Federação") #inserindo mais um item na lista python
print("Colunas Usaveis")
print(colunasUsaveis[:5])

print("Dados Usaveis")
dadoUsaveis = dados[colunasUsaveis] # o conjunto da dados agora será apenas sobre as colunas com dados válidos
print(dadoUsaveis.head)

print("Dados Usaveis com novo indice, Unidade da Federação")
dadoUsaveis = dadoUsaveis.set_index("Unidade da Federação") # alterando o indece do dataframe
print(dadoUsaveis.head)


#localizando dados da linha pelo indice
print("Dados do Ceará")
print(dadoUsaveis.loc["23 Ceará"])

#localizando dados pelo número da linha
print("Dados linha 2")
print(dadoUsaveis.iloc[1]) # o indice do número de linhas inicia com zero

#criando um gráfico
print("Exibindo gráfico....")
dadoUsaveis = dadoUsaveis.drop( #removendo coluna de 'Total'
    "Total", 
    axis=1 # importante para saber que esta a procurar de remover uma coluna do dataframe
    )
dadoUsaveis.T.plot(
    figsize=(12,6) # definindo tamanho
)
plt.show()

### Desafio
###     Reposicionar a legenda
###     Retocar Título da nossa visualização
###     Colocar titulos nos dois eixos