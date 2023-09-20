import numpy as np
a=np.array([[1,2,3,6],[9,8,2,3],[1,7,2,3],[16,4,2,3]])
b=np.sort(a)
print(b)
#column base sort & desc
c=np.sort(a,axis=0)[::-1]
print(c)