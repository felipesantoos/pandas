import pandas as pd
import shutil

teams = {
    "name": ["Atlético-MG", "Flamengo", "Palmeiras", "Corinthians"],
    "titles": [1, 6, 4, 8]
}

df = pd.DataFrame(teams)

print(df.loc[0]) # Retorna um Pandas Series.
print("-" * (shutil.get_terminal_size().columns))
print(df.loc[[0, 1]]) # Retorna um Pandas DataFrame.
