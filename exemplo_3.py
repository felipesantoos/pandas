import pandas as pd

array = [1, 3, 5, 7, 9]
serie = pd.Series(array)

print(serie)

print(serie[0], serie[2], serie[4]) # 1 5 9
