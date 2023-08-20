import pandas as pd

column_names=["A","B","C","D","E"]
indices=[1,2,3,4,5,6,7]

df=pd.DataFrame(columns=column_names,index=indices)
print("The empty dataframe is:")
print(df)

dropdf = df.dropna()
print(dropdf)


column_names=["A","B","C","D","E"]
indices=[1,2,3,4,5,6,7]

df=pd.DataFrame(columns=column_names,index=indices)
print("The empty dataframe is:")
print(df)

fillDf=df.fillna("Auto")
print(fillDf)


