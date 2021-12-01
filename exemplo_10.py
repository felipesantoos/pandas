import pandas as pd

df = pd.read_csv("data.csv")

print(df) # 5 primeiras e 5 últimas linhas.
print(df.to_string()) # Imprime todo o DataFrame.
# Mostra o número máximo de linhas retornada pelo sistema sem precisar do to_string().
print(pd.options.display.max_rows)

pd.options.display.max_rows = 200 # Altera o número máximo de linhas retornadas.

print(df) # Mostra todas as 169 linhas.
