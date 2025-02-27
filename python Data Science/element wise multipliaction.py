# Replace ___ with your code
import numpy as np

# take user input
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))

# create two NumPy arrays from two lists
a1 = np.array(list1)
a2 = np.array(list2)

# use the * operator to multiply two arrays
product = a1*a2
print(product)

# use the multiply() function to multiply two arrays
product = np.multiply(a1,a2)
print(product)