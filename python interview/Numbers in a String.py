# Complete the code below

# define a function
def camel_to_snake_case(string):

    result = ""

    for char in string:
        if char>= 'A' and  char <= 'Z':
            result = result + "_"+char.lower()
        else:
            result += char
    return result

# call the function
string = input()
result = camel_to_snake_case(string)
print(result)