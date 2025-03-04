import calcluatorModel as cm


while(True):
    print("enter mathone operation")
    expression = input()
    if (expression == "exit"):
        break

    data = cm.stringToNumericalData(expression)