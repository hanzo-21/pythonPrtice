


def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    try:
        div= x/y
        return div
    except ZeroDivisionError:
        print("Denominator cannot be 0. Try again")