
print("Введите число:")
x = int(input())
print("Введите количество умножений:")
y = int(input())

def z8(a, b):
    zadanie = [a*i for i in range(1, b+1)]
    return zadanie
print(z8(x, y))
