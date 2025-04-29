# Complete the code below

# define a function
def vowel_repeater(string, n):

    result = ""
    vowels = "AEIOUaeiou"

    for char in string:
        if vowels.__contains__(char):
            for i in range(n):
                result += char
        else:
            result+=char
    return result

# call the function
string = input()
n = int(input())
result = vowel_repeater(string, n)
print(result)