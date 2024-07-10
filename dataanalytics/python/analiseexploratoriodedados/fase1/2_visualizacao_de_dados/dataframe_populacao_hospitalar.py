import pandas as pd
import numpy as np

class DataFramePopulacaoHospitalar:

    #CSV_PATH = 'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_processamento.csv'
    CSV_PATH = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\sih_cnv_qiuf_ano_mes_processamento.csv'

    def __init__(self, csv_path=CSV_PATH):
        self.csv_path = csv_path

    def to_dataframe(self):

        #criando um dataframe
        dados = pd.read_csv(
              self.csv_path 
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

        dadoUsaveis = dados[colunasUsaveis] # o conjunto da dados agora será apenas sobre as colunas com dados válidos
        dadoUsaveis = dadoUsaveis.set_index("Unidade da Federação") # alterando o indece do dataframe
        np.random.seed(524387)

        dadoUsaveis["Total"] = dadoUsaveis.sum(axis=1) #adicionando no final uma coluna de total

        ordenadosPorTotal = dadoUsaveis.sort_values(by="Total", ascending=False)
        ordenadosPorTotal = ordenadosPorTotal.drop("Total", axis=1)

        colunasInteressadas = ordenadosPorTotal.columns[-60:]

        ordenadosPorTotal = ordenadosPorTotal / 1_000_000 # para ter o valor por milhão
        ordenadosPorTotal = ordenadosPorTotal[colunasInteressadas]        

        #mesMaisRecente = ordenadosPorTotal.columns[-1]
        #gastosMaisRecente = ordenadosPorTotal[mesMaisRecente]

        return pd.DataFrame(ordenadosPorTotal)
