# replace ___ with your code

# define a function that takes secret and guess
# and returns the number of bulls and cows
def bulls_and_cows(secret, guess):

    # initialize 0 bulls and cows
    bulls, cows = 0, 0

    # loop from 0 to length of secret
    for i in range(0,len(secret)):

        # if the digits at same index in
        # secret and guess are equal
        # increment bulls
        asec= secret[i]
        bgus = str(guess[i])
        if secret[i] == guess[i]:
            bulls += 1

        # if the digits are not equal at same index
        # check if the current secret digit is in guess
        else:

            # if the current secret digit is in guess
            # increment cows
            
            if secret.find(guess[i]) != -1:
                cows += 1


    # print the bulls and cows numbers in required format
    print(str(bulls)+"A"+str(cows)+"B")


# define secret and guess
# and call the function
secret = '1807'
guess = '7810'
bulls_and_cows(secret, guess)