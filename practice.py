#numpy practice 
import numpy as np
#joining two arrays via concatenate() function
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1,arr2))
print(arr3)
#joining a two dimensional array via concatenate() function
arr4 = np.array([[1,2],[3,4]])
arr5 = np.array([[5,6],[7,8]])
arr6 = np.concatenate((arr4,arr5),axis=1) #axis=1 means joining the arrays column-wise while axis=0 means joining the arrays row-wise
print(arr6) 
#joining the arrays by stack() function
arr7 = np.stack((arr4,arr5),axis=0)
print(arr7)
#splitting an array via array_split() function
arr8 = np.array_split(arr6,2,axis=0)
print(arr8) 
#accesing the splited array
print(arr8[0])
print(arr8[1])
#splitting a 2-d array
arr9 = np.array_split(arr4,2,axis=0)
print(arr9)
#searching an array via where() function
x = np.where(arr5==7)
print(x)
#finding indexes where values are even
y = np.where(arr5%2==0)
print(y)
#using searchsorted() function
z = np.searchsorted(arr1,1)
print(z)
#sorting an array via sort() function
arr10 = np.array([3,5,7,7,6,9,4,2,1,0,8])
arr11 = np.sort(arr10)
print(arr11)
#filtering an array
arr12 = np.array([34,66,78,29])
a = [True, False, True, False]
arr13 = arr12[a]
print(arr13)
