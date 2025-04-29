# replace ___ with your code

# define a function that takes a character as input
# and returns the encrypted character
def encrypt(character):

    # if the character is 'z',
    # assign 'a' to secret
    if character =='z':
        secret = 'a'

    # if the character is 'Z',
    # assign 'A' to secret
    elif character =='Z':
        secret = 'A'
        
    # if the character is not 'z',
    # convert the character in ASCII format, add 1 to it
    # again convert it to character and assign to secret
    else:
        character = ord(character)
        character +=1
        secret = chr(character)

    # return the secret string
    return secret


# define the main function
def main_runner(string):

    # initialize the encrypted string
    result = ''

    # loop through each character in the string
    for char in string:

        # if the character is the alphabet,
        # call the encrypt function and concat the result to result
        if char.isalpha():
            result  += encrypt(char)

        # if the character is not an alphabet,
        # concat the character as it is to result
        else:
            result +=char

    # return the result
    return result


# encrypt message in lowercase
encrypted = main_runner('i am lazy')
print(encrypted)

# encrypt message in uppercase
encrypted = main_runner('I AM LAZY')
print(encrypted)