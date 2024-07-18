import pandas as pd

# Caminho para o arquivo CSV
file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\Producao.csv'

# Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
df = pd.read_csv(file_path, header=None, delimiter=';')

# Contar o número de colunas
num_columns = df.shape[1]

# Ajustar o cabeçalho com base no número de colunas
# Primeiro ao terceiro são fixos, o restante são os anos, a parte 1970
header = ['index', 'cod_produdo','desc_produto'] + [str(year) for year in range(1970, 1970 + num_columns - 3)]

# Adicionar o cabeçalho ao dataframe
df.columns = header

# Salvar o dataframe com o novo cabeçalho
output_path = 'Producao_com_cabecalho.csv'
df.to_csv(output_path, index=False, sep=';')

print(f'Arquivo salvo como {output_path}')