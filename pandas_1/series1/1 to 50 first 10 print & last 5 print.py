import numpy as np
import pandas as pd
a=pd.Series(np.arange(1,51))  #or ([i for i in range(1,51)])
print(a.head(10))
print(a.tail(5))