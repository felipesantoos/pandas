import pandas as pd
import shutil as sh

langs = {
    "name": ["Go", "Python", "TypeScript", "PHP"],
    "score": [10, 9, 10, 6]
}

df = pd.DataFrame(langs, index = ["lang1", "lang2", "lang3", "lang4"])

print(df.loc["lang2"]) # Retorna um Pandas Series.
print("-" * sh.get_terminal_size().columns)
print(df.loc[["lang3", "lang4"]])
