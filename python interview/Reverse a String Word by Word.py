# replace ___ with your code

# function that reverses a string word by word
def reverse_by_word(sentence):

    # split the sentence into words
    words_list = sentence.split(" ")

    # reverse the words in the list
    words_list.reverse()

    # join the words in the list into a sentence
    result = ' '.join(word for word in words_list)


    print(result)


# call the function with the parameter
reverse_by_word('this is blue')