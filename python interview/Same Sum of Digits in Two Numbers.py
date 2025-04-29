# Complete the code below

# define a function
def is_equal(first_number, second_number):

    sum1 = 0
    sum2 = 0

    for n in first_number : 
        sum1 += int(n)
    
    for n in second_number :
        sum2 += int(n)

    return True if sum1 == sum2 else False

# call the function
first_number = input()
second_number = input()
result = is_equal(first_number, second_number)
print(result)