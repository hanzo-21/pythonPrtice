# Complete the function below

# define a function
def unique_character(string):

    string = string.lower()

    for i in range(0,len(string)-1):
        slicedString = string[i+1:len(string)]

        if not(string[i] in slicedString):
            return i
    
    return 0



# call the function
string = input()
result = unique_character(string)
print(result)