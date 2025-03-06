# replace ___ with your code

# define a function that can add any number of arguments
def adder(*num):

    # initialize the sum variable
    sum = 0

    # loop through the arguments and add them to the sum variable
    for n in num:
        sum += n

    # print the sum
    print(sum)


# call the function
adder(1, 2, 3, 4, 5)