import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/missing_data1.csv')
print(df)
print(df.shape)
print(df.head())
print(df.tail())
print(df.isna().sum())
df1=df.fillna(300)
print(df1.isna().sum())
print(df1)