# replace ___ with your code

# function that sums the odd factors of a number
def odd_factor_sum(number):

    # initialize factors list to store all factors
    factors = []

    # start loop from 1 to number
    for num in range(1,number+1):

        # if the number is divisible by i, add i to the factors list
        if number% num ==0 :
            factors.append(num)

    # initialize sum to 0
    sum = 0

    # loop through factors list
    for num in factors:

        # if i is odd, add i to sum
        if num %2 != 0 :
            sum = sum + num

    # print the sum
    print(sum)


# call the function
num = 18
odd_factor_sum(num)