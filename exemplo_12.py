import pandas as pd

disciplines = {
    "name":{
        "0": "SOCO",
        "1": "AOCO",
        "2": "LP",
        "3": "MSI",
        "4": "FUGO"
    },
    "professor":{
        "0": "Sante",
        "1": "Fernando",
        "2": "Maurício",
        "3": "Alagoano",
        "4": "Marcelo"
    },
    "day":{
        "0": "Segunda-feira",
        "1": "Terça-feira",
        "2": "Quarta-feira",
        "3": "Quinta-feira",
        "4": "Sexta-feira"
    }
}

df = pd.DataFrame(disciplines)

print(df)
