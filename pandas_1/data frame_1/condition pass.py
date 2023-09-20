import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/sample4.txt',header=None)
df.columns=['id','fname','lname','age','phno','loc']
#print(df)
df1=df.loc[df['age']>23]
print(df1)

#age equal 24 to fn,ln,age,phno
'''df2=df.loc[df['age']==24] [['fname','lname','age','phno']]
#or
df3=df2[['fname','lname','age','phno']]
print(df3)'''

#chennai work fn,,ln,age,phno,loc
'''df2=df.loc[df['loc']=='Chennai'] [['fname','lname','age','phno','loc']]
print(df2)'''

#chennai work 1 row,id ,fn,ln,age,phno,loc
'''df2=df.loc[df['loc']=='Chennai'].iloc[-1,:]
print(df2)'''