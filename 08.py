print("Введите число:")
x = int(input())
print("Введите количество умножений:")
y = int(input())

def func(a, b):
    array=[]
    for i in range(1, b+1):
        array.append(a*i)
    return array
print("Перемножение числа", x,",", y, "раз, выглядит как:", func(x, y))

