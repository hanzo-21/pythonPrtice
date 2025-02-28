import numpy as np

# create array A with numbers from 1 to 10 using arange()
A = np.arange(1,11)

# create array B with numbers from 11 to 20 using arange()
B = np.arange(11,21)

# add A and B element-wise
C = A+B

# square each element of C
D = C**2

# calculate the sum of all elements in D
sum = np.sum(D)

# print the final sum
print(sum)