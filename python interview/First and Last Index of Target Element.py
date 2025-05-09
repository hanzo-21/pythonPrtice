# replace ___ with your code

# define a function that finds the
# first and last occurences of target element in a list
def first_and_last(num_list, target_element):

    # initialize variables for first and last indexes
    first = None
    last = None

    # loop through the list using enumerate function
    # so that we can also access index
    for i,num in enumerate(num_list):

        # if the target element is found
        if num==target_element:

            # if first index is not set for first time,
            # then only set it to the current index
            if first == None:
                first = i

            # set the last index to the current index
            # every time the target element is found
            last = i

    # return the first and last indexes as tuples
    return (first,last)


# call the function
numbers = [1, 5, 6, 7, 8, 2, 7, 9, 1]
target = 7
result = first_and_last(numbers, target)
print(result)