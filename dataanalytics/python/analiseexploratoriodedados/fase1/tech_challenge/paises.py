import os
import pandas as pd

def listar_paises_unicos(diretorio):
    paises = set()  # Usar um conjunto para evitar duplicações

    for arquivo in os.listdir(diretorio):
        if arquivo.startswith("Imp") and arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(diretorio, arquivo)
            try:
                df = pd.read_csv(caminho_arquivo, delimiter=';', usecols=['pais'], engine='python')  # Ler a coluna "pais"
                if not df.empty:
                    paises.update(df['pais'].dropna().unique())  # Adicionar países únicos ao conjunto
                    print(f"Processado arquivo: {arquivo}")
                else:
                    print(f"Arquivo {arquivo} está vazio ou não contém dados na coluna 'pais'.")
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")

    return paises

def salvar_paises_em_csv(paises, arquivo_saida):
    if paises:
        paises = sorted(paises)

        df_paises = pd.DataFrame(paises, columns=['Pais'])
        df_paises.to_csv(arquivo_saida, index=False)
        print(f"Lista de países única foi salva em '{arquivo_saida}'.")
    else:
        print("Nenhum país foi encontrado nos arquivos CSV fornecidos.")

diretorio = 'C:\\projetos\\wisdombox\\dataanalytics\\python\\analiseexploratoriodedados\\fase1\\tech_challenge\\dados\\'
arquivo_saida = diretorio+'paises.csv'
paises = listar_paises_unicos(diretorio)

salvar_paises_em_csv(paises, arquivo_saida)
