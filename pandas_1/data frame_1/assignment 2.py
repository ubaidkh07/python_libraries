#movies
import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/movies.csv',header=None)
df.columns=['mid','mname','year','rtng','dur']
print(df)
#1)
print(df.shape[0])
#2)
print(df.drop_duplicates().shape[0])
#3)
df1=df.sort_values(by='year',ascending=False)
print(df1)
#4)
df2=df.sort_values(by='rtng',ascending=False).head(5) [['mname','year','rtng']]
print(df2)
#5)
df3=df.sort_values(by='rtng').head(3) [['mname','year','rtng']]
print(df3)
#6)
df4=df.value_counts('year').sort_values(ascending=False)
print(df4)
#7)
df5=df.value_counts('rtng').sort_values(ascending=False)
print(df5)
#8)
df6=df.loc[(df['year']==2008)&(df['rtng']>3)]
print(df6)
#8A)
print(df6.shape[0])
#9)
df7=df.sort_values(by='dur',ascending=False).head(1) [['mname','year','rtng','dur']]
print(df7)
#10)
df8=df.sort_values(by='rtng').head(1) [['mname','year','rtng','dur']]
print(df8)
#11)
df9=df.loc[(df['rtng']>4)&(df['year']==2005)]
print(df9)
#11A)
df10=df9.sort_values(by='rtng',ascending=False)
print(df10)
#11B)
df11=df9.sort_values(by='rtng')
print(df11)
#12)
df12=df.loc[df['year']==2008].value_counts('mname').count()
print(df12)
#13)
df13=df.loc[(df['year']>1975)&(df['year']<2000)]
print(df13)
#13A)
print(df13.shape[0])
#14)
df14=df.loc[(df['year']>1975)&(df['year']<2000)&(df['rtng']>3.5)]
print(df14.shape[0])