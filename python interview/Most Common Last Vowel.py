# Complete the code below

# define a function
def count_common_vowel(string):

    vowelList = ['a','e','i','o','u']
    count = [0,0,0,0,0]

    words = string.split()

    for word in words:
        char = word[len(word)-1]
        if not ('aeiou'.__contains__(char)):
            continue
        index = vowelList.index(char)
        count[index] += 1
    
    maximum = max(count)

    index = count.index(maximum)

    return vowelList[index]



    





# call the function
string = input()
result = count_common_vowel(string)
print(result)