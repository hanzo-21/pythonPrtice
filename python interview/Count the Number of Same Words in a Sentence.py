# Complete the code below

# define a function
def same_word_counter(string):

    #removing special chars
    temp=""

    for char in string:
        if char.isalpha() or  char.isspace():
            temp+=char

    temp = temp.lower()
    words = temp.split(" ")

    wordCount = {}

    for word in words:
        wordCount.update({word : wordCount.get(word,0) +1})
    
    return wordCount






# call the function
string = input()
result = same_word_counter(string)
print(result)