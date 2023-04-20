import pandas as pd

df=pd.read_csv('data.csv')
df['diagnosis'] = df['diagnosis'].astype('category')
df['diagnosis'] = df['diagnosis'].cat.codes
print(df)