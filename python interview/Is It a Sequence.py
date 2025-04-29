# Complete the code below

# define a function
def is_sequence(number_list):
    number_list = list(map(int , number_list))
    difference = number_list[1] - number_list[0]

    for i in range(1, len(number_list)-1):
        if(number_list[i+1] - number_list[i] != difference):
            return False
    
    return True



# call the function
number_list = input().split()
result = is_sequence(number_list)
print(result)