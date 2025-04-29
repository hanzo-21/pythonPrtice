# Complete the code below

# define a function
def sum_of_odd_and_even(lst):
    evenSum =0 
    oddSum = 0

    for num in lst:
        if(num%2 ==0 ):
            evenSum += num
        else: 
            oddSum += num
    
    return(oddSum , evenSum)


# call the function
lst = input().split()
int_list = [int(x) for x in lst]
result = sum_of_odd_and_even(int_list)
print(result)