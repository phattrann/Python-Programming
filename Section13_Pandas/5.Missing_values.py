import pandas as pd 

df = pd.read_csv("pokemon.csv")
# print(df.head())

# isnull
print(df.isnull())

# dropna
# print(df.dropna(inplace = True)) # drop whole row if NaN in rows
# print(df.head())

# fillna
print(df.fillna(1))

# interpolate
print(df.interpolate("linear"))
