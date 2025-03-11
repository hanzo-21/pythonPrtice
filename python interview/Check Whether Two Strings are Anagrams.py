# replace ___ with your code

# define a function that checks
# if the strings are anagrams or not
def is_anagram(str1, str2):

    # remove spaces from the strings
    str1.strip()
    str2.strip()

    # sort the strings
    str1 = sorted(str1)
    str2 = sorted(str2)
    # check if the strings are anagrams or not
    if str2==str1:
        print('The two strings are anagrams')
    else:
        print('The two strings are not anagrams')


# call the function
is_anagram('listen', 'silent')