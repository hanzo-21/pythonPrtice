# Replace ___ with your code
import numpy as np
list1 = list(map(int, input().split()))
# create a NumPy array
array1 = np.array(list1)

# slice the array to select elements at even indices
even_indices = array1[::2]

# reverse the order of the new array
reversed_arr = even_indices[::-1]

# print the resulting array
print(reversed_arr)