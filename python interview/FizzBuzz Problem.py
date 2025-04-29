"""
Write a Python program that returns a string representation of numbers 1 to n.

But instead of numbers that are divisible by 3, it should print 'Fizz' 
and instead of numbers that are divisible by 5, it should output 'Buzz'.
"""

# Complete the function below

# define a function
def fizzbuzz(n):
    resultList = []

    for num in range (1,n+1):
        if(num % 3==0):
            resultList.append("Fizz")
        elif(num%5==0):
            resultList.append("Buzz")
        else:
            resultList.append(str(num))
    
    return resultList


# call the function
number = int(input())
output = fizzbuzz(number)
print(output)