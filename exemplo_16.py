import pandas as pd
import shutil as sh

df = pd.read_csv("dirtydata.csv")
print(df.to_string())

print("-" * sh.get_terminal_size().columns)

new_df = df.dropna()
print(new_df.to_string())

print("-" * sh.get_terminal_size().columns)

df.dropna(inplace = True)
print(df)
