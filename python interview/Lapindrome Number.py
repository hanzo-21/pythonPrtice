# Complete the code below

# define a function
def is_lapindrome(number):

    firstHalf= number[0:int(len(number)/2)]
    secondHalf = number[int(len(number)/2) : int(len(number))]

    for num in  firstHalf:
        if secondHalf.__contains__(num):
            secondHalf.replace(num,"")
        else:
            return "It is not Lapindrome Number"

    return "It is Lapindrome Number"

# call the function
number = input()
result = is_lapindrome(number)
print(result)
