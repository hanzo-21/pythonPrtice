# replace ___ with your code

# define a list
numbers = [51, 51, 23, 6, 5, 2]

# initialize the second largest element
second_largest = 0

# sort the numbers in descending order
numbers.sort(reverse= True)

# compare elements next to each till we find different elements
for i in range(0,len(numbers)-1):
    
    # if the current element and next element are the same,
    # then continue the loop
    if numbers[i] == numbers[i+1]:
        continue
    
    # if the current and next element is not the same,
    # then next element is the second largest element
    second_largest = numbers[i+1]

    # terminate the loop
    break
    
# print the second largest element
print(second_largest)