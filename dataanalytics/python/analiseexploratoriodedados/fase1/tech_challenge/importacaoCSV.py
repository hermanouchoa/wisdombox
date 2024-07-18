import pandas as pd
import os

# Caminho para o arquivo CSV
#file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dadosbrutos\\Producao.csv'
#new_file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dados\\'

file_path = 'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dadosbrutos\\'
new_file_path = 'C:\\projetos\\hermanouchoa\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dados\\'



arquivos_com_prefixo = []
for arquivo in os.listdir(file_path):
    if arquivo.startswith("Imp") and arquivo.endswith('.csv'):
        file = arquivos_com_prefixo.append(arquivo)
        print("file")
        print(arquivo)

        # Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
        df = pd.read_csv(file_path+arquivo, header=None, delimiter=';')
    
        # Contar o número de colunas
        num_columns = df.shape[1]

        # Ajustar o cabeçalho com base no número de colunas
        # Primeiro e segundo são fixos, o restante são os anos, a partir de 1970
        header = ['index', 'pais'] + [str(year) for year in range(1970, 1970 + num_columns - 2)]

        # Adicionar o cabeçalho ao dataframe
        df.columns = header

        # Salvar o dataframe com o novo cabeçalho
        output_path = new_file_path+arquivo+'_ok.csv'
        df.to_csv(output_path, index=False, sep=';')

        print(f'Arquivo salvo como {output_path}')