import numpy as np

# take 8 user inputs and create an array
input_array = list(map(int, input().split()))
                 
# reshape the 1D array into 2D array with shape (2, 4)
# use the argument 'order' to reshape the array in row-wise
arr = np.reshape(input_array,(2,4))

# print the new array
print(arr)