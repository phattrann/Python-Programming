import pandas as pd

df = pd.read_csv("covid19_tweets.csv")
print(df.head())

## Access elements
df.iloc[0] # ACcess a whole row
print(df.iloc[0,1])
print(df.loc[0, 'user_name'])


## Append row
# Append Series, Dataframe
x = pd.Series([1], name = "anything")
df = df.append(x)
# print(df.append(x))

# Insert column
df.insert(loc = 2, column = "anyone", value = 5) # loc or iloc is good as well
# print(df.head())

## Remove (pop, drop)
# df= df.drop(labels = 0)
print(df.drop(labels = 0))

## Rename
print(df.rename(columns = {"anyone" : "hi"}))

## Set index
print(df.set_index("user_name"))