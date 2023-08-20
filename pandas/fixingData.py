import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))

for x in df.index:
    if df.loc[x, " Salary"] > 55000:
        df.loc[x, " Salary"] = 75000

print(df.head(10))
