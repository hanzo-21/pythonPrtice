# Complete the code below

# define a function
def words_start_with(string, letter):
    words = string.split()
    matchList = []

    for word in words:
        if  word[0] == letter:
            matchList.append(word)
    
    return matchList




# call the function
string = input()
letter = input()
result = words_start_with(string, letter)
print(result)