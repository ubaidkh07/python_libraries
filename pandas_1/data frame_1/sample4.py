import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/sample4.txt',header=None)
df.columns=['id','fname','lname','age','phno','loc']
print(df)
#each loc count
df1=df.groupby('loc') ['loc'].count().sort_values(ascending=False)
print(df1)