import pandas as pd

# Caminho para o arquivo CSV
file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dadosbrutos\\Producao.csv'
new_file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dadosbrutos\\'

# Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
df = pd.read_csv(file_path, header=None, delimiter=';')

# Contar o número de colunas
num_columns = df.shape[1]

# Ajustar o cabeçalho com base no número de colunas
# Primeiro ao terceiro são fixos, o restante são os anos, a partir de 1970
header = ['index', 'classificacao','nome_classificacao'] + [str(year) for year in range(1970, 1970 + num_columns - 3)]

# Adicionar o cabeçalho ao dataframe
df.columns = header

# Adicionar a nova coluna "classe" na segunda posição
def classify(row):
    classificacao = row['classificacao']
    if classificacao.startswith('vm'):
        return 'VINHO DE MESA'
    elif classificacao.startswith('vv'):
        return 'VINHO FINO DE MESA (VINÍFERA)'
    elif classificacao.startswith('su'):
        return 'SUCO'
    elif classificacao.startswith('de'):
        return 'DERIVADOS'
    else:
        return 'OUTRO'

df['classe'] = df.apply(classify, axis=1)

# Reorganizar as colunas para que "classe" esteja na segunda posição
cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index('classe')))
df = df[cols]

# Salvar o dataframe com o novo cabeçalho
output_path = new_file_path + 'Producao_ok.csv'
df.to_csv(output_path, index=False, sep=';')

print(f'Arquivo salvo como {output_path}')
