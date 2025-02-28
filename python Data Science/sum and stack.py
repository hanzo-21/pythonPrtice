import numpy as np

# take two arrays as user input
array1 = np.array(list(map(int, input().split())))
array2 = np.array(list(map(int, input().split())))

# calculate the sum of each array 
sum1 = np.sum(array1)
sum2= np.sum(array2)

# stack the resulting arrays together 
arr = np.stack((sum1,sum2),axis=0)
# print the stacked array
print(arr)