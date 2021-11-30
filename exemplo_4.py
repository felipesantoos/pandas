import pandas as pd

array = [1, 3, 5, 7, 9]
serie = pd.Series(array, index=["first", "second", "third", "forth", "fifth"])

print(serie)
print(serie["first"], serie["third"], serie["fifth"]) # 1 5 9
