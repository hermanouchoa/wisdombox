# pip install pandas
# pip install numpy
# pip install matplotlib
import os
import pandas as pd

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

class DataFrameDiabetes:

    CSV_PATH = os.getenv('PATH_DADOS_ML')+"\\diabetes.csv"    
    
    def __init__(self, csv_path=CSV_PATH):
        self.csv_path = csv_path

    def to_dataframe(self):
    
        print("Path Dados: "+self.csv_path)

        df_diabetes = pd.read_csv(self.csv_path, sep=",")

        return pd.DataFrame(df_diabetes)
