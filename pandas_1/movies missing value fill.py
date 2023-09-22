import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/movies.csv',header=None)
df.columns=['id','mname','year','rtng','dur']
print(df)
print(df.isna().sum())
x=df['rtng'].mean()
print(x)
df['rtng'].fillna(3.45,inplace=True)
print(df)
y=df['dur'].mean()
print(y)
df['dur'].fillna(2628.44,inplace=True)
print(df)
print(df.isna().sum())
