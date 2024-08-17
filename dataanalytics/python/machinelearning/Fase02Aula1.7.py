# pip install pandas
# pip install numpy
# pip install matplotlib
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from DataFrameTomates import DataFrameTomates
from DataFrameChess   import DataFrameChess


# Crie uma instância da classe DataFrameTomates
df_tomates = DataFrameTomates()
df_tomates = df_tomates.to_dataframe()
print(df_tomates)

df_chess = DataFrameChess()
df_chess = df_chess.to_dataframe()
print(df_chess)

df_chess.groupby(["victory_status"]).mean(numeric_only=True).plot(kind="pie",y='turns', autopct="%1.0f%%", )
plt.title("Média de partidas dentro do status de vitória")

plt.show()