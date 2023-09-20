import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
print(a[3])
print(a[1:8]) #1,2,3,4,5,6,7
print(a[3:6]) #3,4,5
print(a[:4]) #0,1,2,3
print(a[4:]) #4, to end
print(a[:]) #complete list
print(a[::3]) #complete but step 3 0,3,6,9....
print(a[2:9:2]) #2,4,6,8