# Complete the code below

# define a function
def is_harshad(number):
    temp = int(number)
    sumOfDigit = 0

    while(temp != 0):
        sumOfDigit += (temp % 10)
        temp = int(temp/10)
    
    if(int(number) % sumOfDigit == 0):
        return "It is a Harshad Number"
    else:
        return "It is not a Harshad Number"


# call the function
number = input()
result = is_harshad(number)
print(result)