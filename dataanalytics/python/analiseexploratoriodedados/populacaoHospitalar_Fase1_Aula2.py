#pip install pandas
#pip install matplotlib

# FASE 1 | AULA 2

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
    #, engine='python'
    )

print("Origem do Conjunto de dados - https://datasus.saude.gov.br/informacoes-de-saude-tabnet/")
print("Informações")
print(dados.info())
print("Head")
print(dados.head())

#selecionando uma coluna
print("2008/Ago")
print(dados["2008/Ago"])

#média de uma serie
print("Média de uma serie")
print(dados["2008/Ago"].mean(numeric_only=True))

#criando um gráfico
print("Exibindo gráfico....")
axis = dados.plot(
    x="Unidade da Federação", # eixo "X"
    y="2008/Ago", # eixo "y"
    kind="bar", # tipo de grafico
    figsize=(9,6) # definindo tamanho

)

axis.yaxis.set_major_formatter( ticker.StrMethodFormatter("{x:,.2f}") ) # mudando o formatador no eixo 'Y'
plt.title("Valores por Unidades da Federação")
plt.show()

### Desafio
###     executar o gráfico anterior com o mês mais recente
###     deixar as legendas angulares em 45 graus para facilitar a leitura