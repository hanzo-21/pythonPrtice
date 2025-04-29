# Complete the code below

# define a function
def square_the_lsit(lst):

    sqNum = []

    for num in lst:
        print(pow(num,2))
        sqNum.append(pow(num,2))
    
    sqNum.sort()
    return sqNum


# get input for the list
lst = input().split()

# convert list elements to integer
lst = [int(x) for x in lst]

# call the function
result = square_the_lsit(lst)
print(result)