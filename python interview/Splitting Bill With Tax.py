# Complete the function below

# define a function
def bill_splitter(amount, persons):

    amount += amount * 0.08875

    return amount / persons


# call the function
amount = float(input())
persons = int(input())
result = bill_splitter(amount, persons)
print(result)