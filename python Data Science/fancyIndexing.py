# Replace ___ with your code
import numpy as np

# create a numpy array
arr = np.array([1, 2, 3, 4, 5, 6])

# ask user for integer input 
input_int = int(input())

# use fancy indexing to modify elements at index 1, 3, and 5 with user input integer input_int
arr[[1,3,5]] = input_int
# print the modified numpy array
print(arr)