#Задание 4
print()
print("Задание 4:")
print()

print("Введите число, до которого будут показаны все четные числа:")
x = int(input())

def chet(s):                         #Функция для отбора четных чисел, в заданном диапозоне
    w = [i+1 for i in range(1, s, 2)]
    return w
res = chet(x)
print("В диапозоне от 1 до", x, "следующие четные числа:", res)
print()
