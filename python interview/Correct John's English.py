# Complete the code below

#  define a function that cleans the string
def improve_english(string):
    string = string.lower()
    words = string.split()

    firstWord = words[0]
    res1 = ""
    for i in range(0, len(firstWord)):
        if i ==0:
            res1 = firstWord[i].upper()
            continue
        res1 += firstWord[i]

    words[0] = res1 

    result = words[0] + " "


    for i in range(1,len(words)-1):
        result += words[i] + " "
    
    result += words[len(words)-1] + "."

    return result




# call the function
string = input()
result = improve_english(string)
print(result)