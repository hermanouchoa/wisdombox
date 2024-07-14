
#pip install pandas
#pip install matplotlib
#pip install xlrd

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

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

populacao.columns = ["posicao","uf","populacao","porcentagem","pais_comparavel"]

populacao["populacao"] = populacao["populacao"].str.replace(" ","").astype(int)

populacao = populacao[["uf", "populacao"]]

from dataframe_populacao_hospitalar import DataFramePopulacaoHospitalar
# Crie uma instância da classe DataFrameGenerator
populacaoHospitalar = DataFramePopulacaoHospitalar()
populacaoHospitalar = populacaoHospitalar.to_dataframe()


populacaoHospitalar.index = populacaoHospitalar.index.str[3:] # removendo os três primeiros caracteres do index do dataframe

populacao = populacao.set_index("uf")
populacao.index = populacao.index.str.strip() # removendo espaços em branco do inicio e do fim da string

#existem alguns registro que o nome do estado esta repetido, essa lógica é para ajuste isso
for estado in populacaoHospitalar.index:
    populacao.index = populacao.index.str.replace(f"{estado} {estado}", estado)


#fazendo um join com o dataframe de população hospitalar com a população do IBGE
joinGastosHospitalaresEPopulacao = populacao.join(populacaoHospitalar)

ultimaColuna = joinGastosHospitalaresEPopulacao.columns[-1]
joinGastosHospitalaresEPopulacao["gastos_recentes"] = joinGastosHospitalaresEPopulacao[ultimaColuna] * 1_000_000


joinGastosHospitalaresEPopulacao["gasto_por_habitante"] = joinGastosHospitalaresEPopulacao["gastos_recentes"] / populacao["populacao"]

def insereGastosEGastoPorHabitante(populacaoHospitalar, joinGastosHospitalaresEPopulacao, mes):
    gastos = populacaoHospitalar[mes]
    joinGastosHospitalaresEPopulacao[f"gastos_{mes}"] = gastos
    joinGastosHospitalaresEPopulacao[f"gasto_por_habitante_{mes}"]=joinGastosHospitalaresEPopulacao[f"gastos_{mes}"] / joinGastosHospitalaresEPopulacao["populacao"]
    return joinGastosHospitalaresEPopulacao
    

insereGastosEGastoPorHabitante(populacaoHospitalar, joinGastosHospitalaresEPopulacao, populacaoHospitalar.columns[-1])
insereGastosEGastoPorHabitante(populacaoHospitalar, joinGastosHospitalaresEPopulacao, populacaoHospitalar.columns[-2])
insereGastosEGastoPorHabitante(populacaoHospitalar, joinGastosHospitalaresEPopulacao, populacaoHospitalar.columns[-3])



mensal = populacaoHospitalar.T

meses = {
    "Jan": 1,
    "Fev": 2,
    "Mar": 3,
    "Abr": 4,
    "Mai": 5,
    "Jun": 6,
    "Jul": 7,
    "Ago": 8,
    "Set": 9,
    "Out": 10,
    "Nov": 11,
    "Dez": 12
}

from datetime import date
def para_dia(ano_mes: str):
    ano: int = int(ano_mes[:4])
    mesComoString = ano_mes[5:]
    mes: int = meses[mesComoString]
    return date(ano, mes, 1)

#print(mensal.index.map(para_dia))

mensal.index = mensal.index.map(para_dia)
mensalAberto = mensal.reset_index().melt(id_vars=["index"], value_vars=mensal.columns)
mensalAberto.columns = ["dia_mes_ano", "uf", "gasto"]
mensalAberto["dia_mes_ano"] = pd.to_datetime(mensalAberto["dia_mes_ano"])
mensalAberto["ano"] = mensalAberto["dia_mes_ano"].dt.year
mensalAberto["mes"] = mensalAberto["dia_mes_ano"].dt.month

#mensalAbertoCeara = mensalAberto.query("uf=='Ceará'")

#print(mensalAbertoCeara.head())

# plt.figure(figsize=(10,6))
# axis = sns.lineplot(data=mensalAbertoCeara, x="mes", y="gasto",hue="ano")
# plt.xticks(rotation=30)
# plt.ylim(0,300)
# #axis.xaxis.set_major_locator(ticker.IndexLocator(base=365,offset=0))
# plt.grid(linestyle="--")
# plt.show()


dias_por_mes = {
    1: 31,
    2: 28,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 30,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

mensalAberto["gasto_diario"] = mensalAberto["gasto"] / mensalAberto["mes"].map(dias_por_mes)

#print(mensalAberto.head())

estados = ["Amazonas", "Mato Grosso", "Ceará"]

mensalPorEstado = mensalAberto.query("uf in @estados")
mensalPorEstado = mensalPorEstado.groupby(["uf","ano"]).sum(numeric_only=True)

print(mensalPorEstado)

mensalPorEstado = mensalPorEstado.reset_index()
print("Após reset Index")
print(mensalPorEstado)

#plt.figure(figsize=(10,6))
paleta = sns.color_palette("colorblind", 6)
axis = sns.catplot(
    data=mensalPorEstado, 
    x="ano", 
    y="gasto",
    col="uf",
    kind="bar",
    palette=paleta,
    )
#plt.xticks(rotation=30)
#plt.ylim(0,300)
#axis.xaxis.set_major_locator(ticker.IndexLocator(base=365,offset=0))
#plt.grid(linestyle="--")
plt.show()