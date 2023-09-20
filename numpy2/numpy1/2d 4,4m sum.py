import numpy as np
a=np.array([[2,4,6,8],[1,3,5,7],[3,5,2,1],[5,8,4,6]])
print(a)
b=np.sum(a)
print(b)
c=np.sum(a,axis=1)
print(c)