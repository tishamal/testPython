import pandas as pd

df = pd.read_csv('data.csv')

duplicate = df.duplicated()
noduplicateDf = df.drop_duplicates()

print(df)
print(duplicate)
print(noduplicateDf)

