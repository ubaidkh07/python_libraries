import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/missing_data1.csv')
print(df)
print(df.isna().sum())
#df.dropna(inplace=True,ignore_index=True)
#print(df)
#df.fillna(130,inplace=True)
#print(df)
#print(df)

'''df['Calories'].fillna(250,inplace=True)
print(df)
df['Date'].fillna('2020/12/22',inplace=True)
print(df)
x=df['Calories'].mode()[0]
print(x)'''
#df.dropna(subset=['Calories','Date'],inplace=True)
#print(df)

#find missing values then fill mean value
y=df['Calories'].mean()
for x in df.index:
    if df.loc[x,'Calories']>400:
        df.loc[x,'Calories']=y
print(df)