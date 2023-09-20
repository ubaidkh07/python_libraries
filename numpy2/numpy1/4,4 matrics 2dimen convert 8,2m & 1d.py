import numpy as np
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(a)
b=a.reshape([8,2])
print(b)
c=a.flatten()  #c=a.reshape([16])
print(c)
print(c.ndim)