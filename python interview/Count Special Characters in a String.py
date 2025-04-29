# Complete the function below

# define a function
def character_counter(string):
    specialCharacter =0
    for char in string:
        if  (not char.isalpha()) and (not char.isdigit()) and (not char.isspace()):
            specialCharacter+=1
    
    return specialCharacter


# call the function
string = input()
result = character_counter(string)
print(result)