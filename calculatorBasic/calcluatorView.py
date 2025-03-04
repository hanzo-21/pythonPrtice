import calcluatorModel as cm


def setData(data):
    global number1 ,operator,number2
    number1 = data[0]
    operator = data[1]
    number2 = data[2]

while(True):
    print("enter mathone operation")
    expression = input()
    if (expression == "e"):
        break

    setData( cm.stringToNumericalData(expression))

    match operator:
        case '+':
            result = cm.addition(number1,number2)

        case '-':
            result = cm.subtraction(number1,number2)
        
        case '*':
            result = cm.multiplication(number1,number2)
        
        case '/':
            result = cm.division(number1,number2)

        case _:
            print("something went unexpcted")


    print(expression , " = " , result)