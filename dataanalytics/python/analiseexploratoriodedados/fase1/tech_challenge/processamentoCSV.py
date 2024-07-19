import pandas as pd
import os

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Caminho para o arquivo CSV
file_path = os.getenv('PATH_DADOS_BRUTOS')
new_file_path = os.getenv('PATH_DADOS')


arquivos_com_prefixo = []
for arquivo in os.listdir(file_path):
    if arquivo.startswith("Processa") and arquivo.endswith('.csv'):
        file = arquivos_com_prefixo.append(arquivo)
        print("file")
        print(arquivo)

        # Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
        df = pd.read_csv(file_path+arquivo, header=None, delimiter=';')
    
        # Contar o número de colunas
        num_columns = df.shape[1]

        # Ajustar o cabeçalho com base no número de colunas
        # Primeiro ao terceiro são fixos, o restante são os anos, a partir de 1970
        header = ['index', 'classificacao','nome_classificacao'] + [str(year) for year in range(1970, 1970 + num_columns - 3)]

        # Adicionar o cabeçalho ao dataframe
        df.columns = header

        # Salvar o dataframe com o novo cabeçalho
        output_path = new_file_path+arquivo+'_ok.csv'
        df.to_csv(output_path, index=False, sep=';')

        print(f'Arquivo salvo como {output_path}')