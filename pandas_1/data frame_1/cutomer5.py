import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/customer5.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc','salary']
print(df)
#each prof count(count desc)
df1=df.value_counts('prof').sort_values(ascending=False)
print(df1)
#each prof total salary(salary desc)
df2=df.groupby('prof') ['salary'].sum().sort_values(ascending=False)
print(df2)
#each country max salary(sal desc)
df3=df.groupby('loc') ['salary'].max().sort_values(ascending=False)
print(df3)
#each country avg salary
df4=df.groupby('loc') ['salary'].mean()
print(df4)
#each prof min salary
df5=df.groupby('prof') ['salary'].min()
print(df5)
#each age group total salary
df6=df.groupby('age') ['salary'].sum()
print(df6)