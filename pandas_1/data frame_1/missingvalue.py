import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/customer1.txt',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df.isna().sum())
#fill missing value
df1=df.fillna('india')
print(df1.isna().sum())
