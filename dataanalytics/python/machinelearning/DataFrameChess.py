# pip install pandas
# pip install numpy
# pip install matplotlib
import os
import pandas as pd

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

class DataFrameChess:

    XLS_PATH = os.getenv('PATH_DADOS_ML')+"\\Chess.xlsx"
    
    def __init__(self, xls_path=XLS_PATH):
        self.xls_path = xls_path

    def to_dataframe(self):
    
        print("Path Dados: "+self.xls_path)

        df_chess = pd.read_excel(self.xls_path, sheet_name="Chess")
      
        return pd.DataFrame(df_chess)
