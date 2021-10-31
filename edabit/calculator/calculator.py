import operator

def calculator(x: int, operation: str, y: int):
    try:
        # match-case introduced in python version 3.10
        match operation:
            case '+':
                return x + y
            case '-':
                return x - y
            case '*':
                return x * y
            case '/':
                return x / y
            case '%':
                return x % y
            case '**':
                return x ** y

        # ops = {
        #     '+': operator.add,
        #     '-': operator.sub,
        #     '*': operator.mul,
        #     '/': operator.truediv,
        #     '%': operator.mod,
        #     '**': operator.pow
        #     }
    
        # return ops[operation](x, y)
    except ZeroDivisionError:
        return "Can't divide by 0!"

print(calculator(2, '/', 2))
print(calculator(10, '-', 7))
print(calculator(2, '*', 16))
print(calculator(2, '-', 2))
print(calculator(15, '+', 26))
print(calculator(2, '+', 2))
print(calculator(2, "/", 0))