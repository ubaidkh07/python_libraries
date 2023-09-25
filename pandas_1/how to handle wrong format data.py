import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/movies.csv',header=None)
df.columns=['id','mname','year','rtng','dur']
print(df)

#df.loc[7,'dur']==4.5
print(df)
x=df['rtng'].mean()
y=df['dur'].median()
df['rtng'].fillna(x,inplace=True)
df['dur'].fillna(y,inplace=True)
#external file
print(df.isna().sum())
df.to_csv('/home/ubaid/Downloads/cleaned_movies1.csv',index=False,header=False)