import pandas as pd

data = {"calories": [420, 380, 390,88], "duration": [50, 40, 25,9]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

print(type(df["calories"]))