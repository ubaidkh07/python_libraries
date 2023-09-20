import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/sample4.txt',header=None)
df.columns=['id','fname','lname','age','phno','loc']
df1=df.loc[(df['age']>23)&(df['loc']=='Chennai')]
print(df1)