# Replace ___ with your code
import numpy as np
n = int(input())
# create an array with numbers from 0 to 20 (inclusive)
array1 = np.arange(n)

# set every alternate number to 0
array1[::2] = 0

# print the resulting array
print(array1)