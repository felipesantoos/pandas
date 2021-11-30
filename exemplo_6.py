import pandas as pd

olympics = {
    "country": ["EUA", "China", "Brasil"],
    "gold": [10, 7, 4],
    "silver": [5, 6, 8],
    "bronze": [2, 6, 11]
}

odf = pd.DataFrame(olympics)

print(odf)
