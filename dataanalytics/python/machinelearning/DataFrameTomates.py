# pip install pandas
# pip install numpy
# pip install matplotlib
import os
import pandas as pd

from dotenv import load_dotenv # pip install python-dotenv

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

def categorizar_tomate_media(media):
    if media >= 40 and media <= 70:
        return "tomate medio"
    elif media < 40:
        return "tomate pequeno"
    else: 
        return "tomate grande"

class DataFrameTomates:

    CSV_PATH = os.getenv('PATH_DADOS_ML')+"\\Tomato.csv"    
    
    def __init__(self, csv_path=CSV_PATH):
        self.csv_path = csv_path

    def to_dataframe(self):
    
        print("Path Dados: "+self.csv_path)

        df_tomato = pd.read_csv(self.csv_path, sep=",")

        df_tomato["categoria_tomate"] = df_tomato["Average"].apply(categorizar_tomate_media)

        df_tomato["Date"] = pd.to_datetime(df_tomato["Date"])

        return pd.DataFrame(df_tomato)
