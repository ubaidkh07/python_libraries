import numpy as np
import pandas as pd
df=pd.read_csv('/home/ubaid/Downloads/sample1.txt',header=None)
df.columns=['id1','id2','id3','id4','id5','id6','id7']
print(df)