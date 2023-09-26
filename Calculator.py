def calc():
    try:
        x = int(input("whats val of x? "))
        y = int(input("whats val of y? "))
        op = input("Addition (+)\nSubtraction (-)\nMultiplication (*)\nDivision (/)\nRemainder (%)\nChoose operator: ")
    except ValueError:
        print("Value is not Integer")
    if op == '+': print(x + y)
    elif op == '-': print(x - y)
    elif op == '*': print(x * y)
    elif op == '/': print(x / y)
    elif op == '%': print(x % y)
    else: print('Error')
    
