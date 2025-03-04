opration = "+-*/"
nums = "123456789"


def stringToNumericalData(expression):
    data = [0,0,0]
    numStack=""
    for digit in expression:
        if digit ==' ':
            continue
    
        if nums.__contains__(digit):
            numStack = numStack+digit
        elif opration.__contains__(digit):
            data[0] = int(numStack)
            data[1] = opration.index(digit)
            numStack="" 
    
    if(numStack!=""):
        data[2]=int(numStack)

    return data

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