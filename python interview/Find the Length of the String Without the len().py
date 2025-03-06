# replace ___ with your code

# define a function that prints the length of a string without len() function
def length_of_string(string):

    # define a counter that stores the length of a string
    strlen  = 0

    # loop through each character in the string
    for char in string:

        # for each character, increment the length counter by 1
        strlen +=1

    # print the length counter
    print(strlen)


# call the function
length_of_string('Python')