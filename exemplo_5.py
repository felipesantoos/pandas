import pandas as pd

medals = {
    'china': 32,
    'eua': 21,
    'brasil': 10
}

serie = pd.Series(medals, index=['china', 'brasil'])

print(serie)
