import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/customer1.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc']
df1=df.loc[(df['loc']=='india')&(df['age']>50)].iloc[:,1:5]
print(df1)
