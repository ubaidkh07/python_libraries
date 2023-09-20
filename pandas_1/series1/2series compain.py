import numpy as np
import pandas as pd
a=pd.Series([1,3,4,6,8,9])
b=pd.Series([2,5,4,1,7,6])
c=a._append(b,ignore_index=True)
print(c)