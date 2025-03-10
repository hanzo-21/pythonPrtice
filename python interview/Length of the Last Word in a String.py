# replace ___ with your code

# function that prints length of last word
def length_of_last_word(sentence):
    
    puncutation = ".?/\"\' "

    # split sentence into words
    words_list = sentence.split(' ')

    # get the length of the last word
    result =len(words_list[-1])
    

    # if there is punctuation at the end of the sentence, remove it from the result
    if  puncutation.__contains__(sentence[-1]):
        result =result -1
        


    print(result)


# call the function
length_of_last_word('I love programming')