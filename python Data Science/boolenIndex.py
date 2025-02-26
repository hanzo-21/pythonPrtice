# Replace ___ with your code
import numpy as np
numbers_list = list(map(int,input().split()))
# create an array of numbers
numbers = np.array(numbers_list)

# select only the odd numbers from the array
odd_numbers = numbers[numbers%2!=0]

# print the resulting value
print(odd_numbers)