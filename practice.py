import numpy as np
arr = np.array([[1,2,4,3,5],[6,7,8,9,10],[11,12,13,14,15]])
print(arr)

print(arr.ndim)
print(arr.shape)
#creating an array object
print(type(arr))
#accessing an array element
print(arr[1,1])
#accessing an array using negative indexing
print(arr[-2,-4])
#slicing an array
print(arr[0:2,1:4])
#negative slicing of an array
print(arr[-2:,-4:])
#checking the datatype of an  array
print(arr.dtype)
#creating arrays with defined datatypes using dtype argument.
arr1 = np.array([1,2,3,4], dtype='S')
print(arr1)
print(arr1.dtype)
#converting datatype on existing array using astype() method
arr1 = arr.astype('i')
print(arr1)
print(arr1.dtype)
#copy of an array using copy() method
arr2 = arr.copy()
print(arr2)
arr2[0,0]= 100
print(arr)
#view of an array using view() method
arr3 = arr.view()
print(arr3)
arr3[0,1] = 100
print(arr)
#checking if arrays own its data
print(arr2.base)
print(arr3.base)
#resgaping an array using reshape() method
arr4 = arr.reshape(5,3)
print(arr4)
#using unknown dimensionin reshape() method
arr5 = arr.reshape(5,3,-1)
print(arr5)
