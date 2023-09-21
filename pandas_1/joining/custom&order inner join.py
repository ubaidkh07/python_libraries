import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/custom_employee.txt',header=None)
df.columns=['id','name','age','loc','salary']
df1=pd.read_csv('/home/ubaid/Downloads/order.txt',header=None)
df1.columns=['oid','date','id','amount']
print(df)
print(df1)
#salary above 2000 name,age,salary,date,amount
df2=pd.merge(df,df1,on='id',how='inner').loc[df['salary']>2000] [['name','age','salary','date','amount']]
print(df2)
#salary above 2000 and amount above 1500 name,age,loc,dat,amount
df3=pd.merge(df,df1,on='id',how='inner').loc[(df['salary']>2000)&(df1['amount']>1500)] [['name','age','loc','date','amount']]
print(df3)
#age mxm 1 employee name,age,salary,date,amount
df4=pd.merge(df,df1,on='id',how='inner').sort_values(by='age',ascending=False).head(1) [['name','age','salary','date','amount']]
print(df4)
#latest date purchace 1 name,age,salary,dat,amount
df5=pd.merge(df,df1,on='id',how='inner').sort_values(by='date',ascending=False).head(1) [['name','age','salary','date','amount']]
print(df5)
#name,age,dat,amount collect
df6=pd.merge(df,df1,on='id',how='inner') [['id','name','age','date','amount']]
print(df6)