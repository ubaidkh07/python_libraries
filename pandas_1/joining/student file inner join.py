import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/student',header=None)
df.columns=['name','rollno']
df1=pd.read_csv('/home/ubaid/Downloads/results',header=None)
df1.columns=['rollno','result']
print(df)
print(df1)
#pass name,roll,result
df2=pd.merge(df,df1,on='rollno',how='inner').loc[df1['result']=='pass'] [['name','rollno','result']]
print(df2)