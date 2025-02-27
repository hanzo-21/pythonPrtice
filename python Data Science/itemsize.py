# Replace ___ with your code
import numpy as np
list1 = list(input().split())
# create a numpy array
array1 = np.array(list1)

# use itemsize to find size of each array element
print(array1.itemsize)

# use nbytes to find the size of the entire array
print(array1.nbytes)