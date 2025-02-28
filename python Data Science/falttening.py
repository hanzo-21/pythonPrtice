import numpy as np

# take array as user input
# can take array of any dimension
array1 = np.array(eval(input()))

# flatten the array column-wise
fla = array1.flatten(order="F")


# print the flattened array
print(fla)