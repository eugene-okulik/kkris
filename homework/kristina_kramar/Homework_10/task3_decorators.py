def decor_operation(func):
    def wrapper(x, y):
        if x == y:
            action='+'
        elif x < 0 or y < 0:
            action='*'
        elif x > y:
            action='-'
        elif x < y:
            action='/'
        return func(x, y, action)
    return wrapper


@decor_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first = int(input('Input first number:'))
second = int(input('Input second number:'))
print(calc(first, second))
