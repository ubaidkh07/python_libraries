import numpy as np
import pandas as pd
a=pd.Series([1,5,6,3,8])
b=pd.Series([3,6,2,9,6])
c=a.add(b)
print(c)
d=a.subtract(b)
print(d)
e=a.multiply(b)
print(e)
f=a.div(b)
print(f)