import pandas as pd

df_csv = pd.read_csv("pandas_data.csv", index_col = "Name")

print(df_csv.loc["Pikachu"])