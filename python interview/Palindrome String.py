"""
Given a string of size n, check if the string is a palindrome by removing all spaces and special characters.

Use the following Python functions to filter the alphabets and digits in the input string:

isalpha() - returns True if the character is alphabet
isdigit() - returns True if the character is digit
"""


# Complete the function below

# define a function
def is_palindrome(string):
    string = string.lower()
    tempStr = ""

    for char in string:
        if(char.isalpha()):
            tempStr += char

    for i in range (0,int(len(tempStr)/2)+1):
        if tempStr[i] != tempStr[len(tempStr)-1-i]:
            return "String is not Palindrome"
    
    return"String is Palindrome"
       


# call the function
string = input()
result = is_palindrome(string)
print(result)