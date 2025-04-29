# Complete the code below

# define a function
def is_armstrong(number):
    temp = int(number)
    sumOfCubeDigit = 0

    while(temp != 0):
        sumOfCubeDigit +=pow((temp % 10),3)
        temp = int(temp/10)
    
    if(int(number) == sumOfCubeDigit ):
        return "It is an Armstrong Number"
    else:
        return "It is not an Armstrong Number"


# call the function
number = input()
result = is_armstrong(number)
print(result)