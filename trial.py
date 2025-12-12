import pandas as pd
import seaborn as sns
df_csv = pd.read_csv("pandas_data.csv", index_col = "Name")

print(df_csv.loc["Pikachu"])