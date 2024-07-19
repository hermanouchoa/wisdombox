import pandas as pd
import os
from unidecode import unidecode

file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dadosbrutos\\'
new_file_path = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dados\\'

mapeamento_pais = {
    "Alemanha, Republica Democratica": "Alemanha",
    "Alemanha, Republica Democratica da": "Alemanha",
    "Cayman, Ilhas": "Ilhas Cayman",
    "Coreia do Sul, Republica da": "Coreia do Sul",
    "Coreia,  Republica Sul": "Coreia do Sul",
    "Dominica, Ilha de": "Ilha de Dominica",
    "Eslovaca,  Republica": "Republica Eslovaca",
    "Falkland (Malvinas)": "Falkland (Ilhas Malvinas)",
    "Marshall, Ilhas": "Ilhas Marshall",
    "Russia,  Federacao da": "Russia",
    "Taiwan (FORMOSA)": "Taiwan (Formosa)",
    "Tcheca, Republica": "Republica Tcheca",
    "Tcheca,  Republica": "Republica Tcheca",
    "Turcas e Caicos, ilhas": "Ilhas Turcas e Caicos",
    "Coreia do Norte, Republica": "Coreia do Norte",
    "Coreia do Sul, Republica": "Coreia do Sul"
}

arquivos_com_prefixo = []
for arquivo in os.listdir(file_path):
    if arquivo.startswith("Imp") and arquivo.endswith('.csv'):
        arquivos_com_prefixo.append(arquivo)
        print("file")
        print(arquivo)

        # Carregar o arquivo CSV sem cabeçalho, usando ";" como delimitador
        df = pd.read_csv(file_path + arquivo, header=None, delimiter=';')
    
        # Contar o número de colunas
        num_columns = df.shape[1]

        # Ajustar o cabeçalho com base no número de colunas
        header = ['index', 'pais'] + [str(year) for year in range(1970, 1970 + num_columns - 2)]

        # Adicionar o cabeçalho ao dataframe
        df.columns = header

        # Remover aspas e caracteres especiais
        for column in df.columns:
            df[column] = df[column].map(lambda x: unidecode(str(x)).replace('"', '').replace("'", ''))

        # Ajustar os valores da coluna "pais"
        df['pais'] = df['pais'].replace(mapeamento_pais)

        # Salvar o dataframe com o novo cabeçalho
        output_path = new_file_path + arquivo + '_ok.csv'
        df.to_csv(output_path, index=False, sep=';')

        print(f'Arquivo salvo como {output_path}')
