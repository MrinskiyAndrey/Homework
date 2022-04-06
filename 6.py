#Задание 6



x = int(input())

def binary(a):
    b = ''
    while a > 0:
        b = str(a % 2) + b
        a = a // 2
    return b
print(binary(x))

