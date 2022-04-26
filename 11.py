data = input('Введите арифметическую операцию\nчерез пробел (например 2 + 3): ')
list_data = data.split()
x = list_data[0]
y = list_data[1]
z = list_data[2]
x = int(x)
z = int(z)


def calc(a, op, b):
    if op == '+':
        operation = (a + b)
    elif op == '-':
        operation = (a - b)
    elif op == '*':
        operation = (a * b)
    elif op == '/':
        if b == 0:
            operation = -1
        else:
            operation = (a / b)
        

    return operation

print(calc(x, y, z))
