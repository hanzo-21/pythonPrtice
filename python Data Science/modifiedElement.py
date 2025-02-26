# Replace ___ with your code
import numpy as np

# create an array of numbers
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# get integer user inputs for even and odd replacement

even_int = int(input())
odd_int = int(input())


# change even numbers with user-specified integer input

numbers[numbers % 2 == 0] = even_int

# change odd numbers with user-specified integer input

numbers[numbers % 2 != 0] = odd_int

# print the modified array
print(numbers)