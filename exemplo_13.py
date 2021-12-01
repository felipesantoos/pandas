import pandas as pd

df = pd.read_csv("data.csv")

# Retorna os cabeçalhos e as n primeiras linhas (5 por padrão).
print(df.head(10))
