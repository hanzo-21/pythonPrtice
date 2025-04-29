# Complete the code below

# define a function
def duplicate_counter(string):
    string = string.lower()
    string = string.replace(" ","")
    encounteredRepeatedChar = ""
    duplicatedChars = 0

    for i in range(0,len(string)):
        sliceString = string[i+1:len(string)]
        if sliceString.__contains__(string[i]) and not encounteredRepeatedChar.__contains__(string[i]):
            duplicatedChars +=1
            encounteredRepeatedChar += string[i]

    return duplicatedChars



# call the function
string = input()
result = duplicate_counter(string)
print(result)