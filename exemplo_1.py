import pandas as pd

mydataset = {
    'name': ["Felipe", "Jesus", "Gabriel", "Rony"],
    'age': [20, 19, 21, 21]
}

mydataframe = pd.DataFrame(mydataset)

print(mydataframe)
