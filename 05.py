#Задание 5

print()
print("Задание 5:")
print()


print("Введите X")
x = int(input())
print("Введите Y")
y = int(input())
               
def cordinate_angle(x, y):
    if x > 0 and y > 0:
        print("Вы ввели координаты угла I")
    elif x < 0 and y > 0:
        print("Вы ввели координаты угла II")
    elif x < 0 and y < 0:
        print("Вы ввели координаты угла III")
    elif x > 0 and y < 0:
        print("Вы ввели координаты угла IV")
    else:
        print("Введены не корректные данные. Введите целые числа")





               
cordinate_angle(x, y)
input()
