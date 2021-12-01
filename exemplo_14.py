import pandas as pd

df = pd.read_csv("data.csv")

# Retorna as n últimas linhas (5 por padrão).
print(df.tail())
