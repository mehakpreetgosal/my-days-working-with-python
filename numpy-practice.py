#practicing pandas 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
#making an 3D array
b = np.array([[[[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]],[[23,24,25,26],[27,28,29,30]]]]],ndmin=5)
print(b)
print(b[0,0,0,0,-1])
print(b[0,0,2,0,-2])
print(b[0,0,2,1,-3])
print(b[0,0,1,0,-4])
#slicing
print(b[0,0,2,0,1:4:2])
#negative slicing
print(b[0,0,0,0,-1:-4:-2])
print(b.dtype)
#changin datatype of an existing array
bb = b.astype('f')
print(bb.dtype)
#copying an array
c = a.copy()
c[0,1] = 169
c[1,0] = 431
print(c)
#viewing
d = a.view()
print(d.base)
#adding unknown dimensions in an array
e = np.array([[1,2,3,4,5],[6,7,8,9,10]],ndmin=-1)
print(e.ndim)
#iteration
for i in a:
    print(i%2)
#shape of an array 
print(a.shape)
#reshaping an array
f = a.reshape(5,2)
print(f)
for x in np.nditer(f):
    print(x)
#joining arrays
g = np.concatenate((a,c), axis=0)
print(g)
h = np.stack((a,c), axis=2)
print(h)
#splitting arrays
i = np.array_split(a, 2, axis=1)
print(i)
#searching an array
print(np.where(b%2==0))
#sorting an array
j = np.array([[3,2,1],[6,5,4]])
print(np.sort(j))
#complete

