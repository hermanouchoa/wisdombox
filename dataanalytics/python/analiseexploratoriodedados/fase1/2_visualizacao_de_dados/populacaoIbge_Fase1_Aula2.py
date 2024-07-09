
#pip install pandas
#pip install matplotlib
#pip install xlrd

import pandas as pd
import matplotlib.pyplot as plt

#path_dados = 'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\estimativa_dou_2020.xls'
#path_dados = "https://github.com/alura-cursos/agendamento-hospitalar/blob/main/dados/estimativa_dou_2020.xls?raw=true"

#ibge_estimativa = pd.read_excel(path_dados)
#print(ibge_estimativa.head())


dados_da_populacao = """Posição	Unidade federativa	População	% da pop. total	País comparável

1	 São Paulo	46 649 132	21,9%	Flag of Spain.svg Espanha (46 439 864)
2	 Minas Gerais	21 411 923	10,1%	 Sri Lanka (20 675 000)
3	 Rio de Janeiro	17 463 349	8,2%	 Países Baixos (16 922 900)
4	Bahia Bahia	14 985 284	7,1%	 Chade (14 037 000)
5	 Paraná	11 597 484	5,4%	 Bolívia (11 410 651)
6	 Rio Grande do Sul	11 466 630	5,4%	 Bélgica (11 250 659)
7	 Pernambuco	9 674 793	4,5%	 Bielorrússia (9 485 300)
8	 Ceará	9 240 580	4,3%	 Emirados Árabes Unidos (9 157 000)
9	Pará Pará	8 777 124	4,1%	 Áustria (8 602 112)
10	 Santa Catarina	7 338 473	3,4%	 Sérvia (7 114 393)
11	 Goiás	7 206 589	3,4%	 Paraguai (7 003 406)
12	 Maranhão	7 153 262	3,4%	 Paraguai (7 003 406)
13	 Amazonas	4 269 995	2,0%	 Líbano (4 168 000)
14	 Espírito Santo	4 108 508	1,9%	 Líbano (4 168 000)
15	 Paraíba	4 059 905	1,9%	 Líbano (4 168 000)
16	 Mato Grosso	3 567 234	1,7%	 Uruguai (3 415 866)
17	 Rio Grande do Norte	3 560 903	1,7%	 Uruguai (3 415 866)
18	 Alagoas	3 365 351	1,6%	 Uruguai (3 415 866)
19	 Piauí	3 289 290	1,6%	 Kuwait (3 268 431)
20	 Distrito Federal	3 094 325	1,4%	 Lituânia (2 900 787)
21	 Mato Grosso do Sul	2 839 188	1,3%	 Jamaica (2 717 991)
22	 Sergipe	2 338 474	1,1%	 Namíbia (2 280 700)
23	 Rondônia	1 815 278	0,8%	 Gabão (1 725 000)
24	 Tocantins	1 607 363	0,7%	 Bahrein (1 359 800)
25	 Acre	906 876	0,4%	 Fiji (859 178)
26	 Amapá	877 613	0,4%	 Fiji (859 178)
27	 Roraima	652 713	0,3%	 Luxemburgo (562 958)"""

# fonte https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o#cite_note-IBGE_POP-1
# fonte indireta IBGE

from io import StringIO
dados_da_populacao_io = StringIO(dados_da_populacao)

novos_dados = pd.read_csv(dados_da_populacao_io, sep="\t")
populacao = novos_dados.dropna()
print("-------------------")
print(novos_dados.head())

populacao.columns = ["posicao","uf","populacao","porcentagem","pais_comparavel"]
print("População")
print(populacao)

print("População - Replace no conteudo da celula na coluna 'populacao'")
populacao["populacao"] = populacao["populacao"].str.replace(" ","").astype(int)
print(populacao.head())

print("População - apenas colunas de 'uf' e 'populacao'")
populacao = populacao[["uf", "populacao"]]
print(populacao.head())

import sys
print(sys.path)

from dataframe_populacao_hospitalar import DataFramePopulacaoHospitalar
# Crie uma instância da classe DataFrameGenerator
df_generator = DataFramePopulacaoHospitalar()
df = df_generator.to_dataframe()

print(df)
