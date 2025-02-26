# Replace ___ with your code
import numpy as np

# take array as user input
numbers = np.array(list(map(int,input().split())))

# slice elements from index 1 to 4
sliced_numbers = numbers[1:4]

print(sliced_numbers)

# slice elements from index 2 to last element
sliced_numbers = numbers[2:]

print(sliced_numbers)

# slice elements from start to end without using any number
sliced_numbers = numbers[:]

print(sliced_numbers)