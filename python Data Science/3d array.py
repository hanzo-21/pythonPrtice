import numpy as np

# take list input
list1 = eval(input())

# create the given array
arr = np.array(list1)
print(arr)
                 
# slice the first matrix
print("first matrix")
print(arr[0,:,:])

# slice the third column of the second matrix
print("second matrix")
print(arr[1,:,2])

# slice the second row of each matrix
print("second row of each matrix")
print(arr[:,1,:])