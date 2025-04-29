# Complete the code below

# define a function
def is_abundant(number):
    sum = 1

    for num in range(2,int(number/2)+1):
        if ( number% num ==0 ):
            sum += num
    
    if sum > number:
        return "It is an Abundant Number"
    else:
        return "It is not an Abundant Number"



# call the function
number = int(input())
result = is_abundant(number)
print(result)