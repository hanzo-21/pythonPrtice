# replace ___ with your code

# define a list of numbers
lst = [1, 0, 2, 0, 4, 0, 6, 5]

# loop through each number in the list
for num in range(0,len(lst)):

    # if the number is 0
    if lst[num]==0:

        # remove the number from the list
        lst.pop(num)

        # also add the number to the end of the list
        lst.append(0)

# print the list
print(lst)