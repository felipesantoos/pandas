import pandas as pd
import shutil as sh

df = pd.read_csv("dirtydata.csv")
print(df.to_string())

print("-" * sh.get_terminal_size().columns)

df["Calories"].fillna(130, inplace = True)
print(df.to_string())
