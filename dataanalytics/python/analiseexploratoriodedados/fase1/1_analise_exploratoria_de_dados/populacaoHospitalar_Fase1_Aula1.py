#pip install pandas
#pip install matplotlib

# FASE 1 | AULA 1

import pandas as pd
import matplotlib.pyplot as plt

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