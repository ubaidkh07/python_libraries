import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/customer1.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)
#df1=df.rename(columns={'loc':'place'})
#print(df1)
#df2=df[['fname','lname','age','prof']]
#print(df2)
#df3=df.iloc[3:7,0:4]
#print(df3)
#x=df.iloc[:,:5]
#print(x)
#y=df.iloc[:,5]
#print(y)
#missing value check
#print(df.isna().sum())
#ecah prof count
'''df1=df.groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df1)'''
#india work each prof count
df1=df.loc[df['loc']=='india'].groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df1)