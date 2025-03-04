operator = "+-*/"
nums = "123456789"


def stringToNumericalData(expression):

    try:

        data = [0,0,0]
        numStack=""
        for digit in expression:
            if digit ==' ':
                continue
        
            if operator.__contains__(digit):
                try:
                    data[0] = int(numStack)
                except ValueError:
                    print("Invaide input")

                data[1] = operator.index(digit)
                numStack=""  

            numStack = numStack+digit
               
                
        
        if(numStack!=""):
            try:
                    data[2] = int(numStack)
            except ValueError:
                    print("Invaide input")

        return data
    
    except:
        print("something went wrong")

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