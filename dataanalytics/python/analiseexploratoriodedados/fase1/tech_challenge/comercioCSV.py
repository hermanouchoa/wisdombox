import pandas as pd
import os

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Caminho para o arquivo CSV
file_path = os.getenv('PATH_DADOS_BRUTOS')+"Comercio.csv"
new_file_path = os.getenv('PATH_DADOS')
#file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dadosbrutos\\Producao.csv'
#new_file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dados\\'

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
    if classificacao.startswith('vm_'):
        return 'VINHO DE MESA'
    elif classificacao.startswith('vfm_'):
        return 'VINHO  FINO DE MESA'
    elif classificacao.startswith('VINHO FRIZANTE'):
        return 'VINHO FRIZANTE'
    elif classificacao.startswith('VINHO ORGÂNICO'):
        return 'VINHO ORGÂNICO'
    elif classificacao.startswith('ve_'):
        return 'VINHO ESPECIAL'
    elif classificacao.startswith('es_'):
        return 'ESPUMANTES'
    elif classificacao.startswith('su_'):
        return 'SUCO DE UVAS'
    elif classificacao.startswith('SUCO DE UVAS CONCENTRADO'):
        return 'SUCO DE UVAS CONCENTRADO'
    elif classificacao.startswith('ou_'):
        return 'OUTROS PRODUTOS COMERCIALIZADOS'
    else:
        return None

df['classe'] = df.apply(classify, axis=1)

# Remover linhas onde a coluna "classe" é None
df = df.dropna(subset=['classe'])

# Reorganizar as colunas para que "classe" esteja na segunda posição
cols = df.columns.tolist()
cols.insert(1, cols.pop(cols.index('classe')))
df = df[cols]

# Salvar o dataframe com o novo cabeçalho
output_path = new_file_path + 'Comercio.csv'
df.to_csv(output_path, index=False, sep=';')

print(f'Arquivo salvo como {output_path}')
