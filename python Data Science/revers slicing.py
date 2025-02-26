# Replace ___ with your code
import numpy as np
list1 = list(map(int,input().split()))

# create the original array
array1 = np.array(list1)

# select the first three elements of the original array using negative indexing
new_arr = array1[0:3:1]

# display resulting array
print(new_arr)