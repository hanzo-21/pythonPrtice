# Complete the code below

# define a function
def semi_reverse(string):
    words = string.split()
    result = ""

    for word in words:
        if(len(word)%2!=0):
            word = word[::-1]
        result = result + word + " "
    return result

        


# call the function
string = input()
result = semi_reverse(string)
print(result)