# Complete the code below

# define a function
def required_fuel(kms):
    return(kms*10 , kms*10 -100 if kms*10 > 100 else 0  )


# call the function
kms = int(input())
result = required_fuel(kms)
print(result)