#Задание 1:
print()
print("Задание 1:")
print()


test_string = 'Just a simple string'
print(test_string[14:20])
print(test_string[0:4])
print(test_string[7:13])
print(test_string[0:20:5])
print(test_string[-21:-1:3])
print()


#Задание 2
print()
print("Задание 2:")
print()

def conv_type(a):                      #Функция для изменения типа данный в строчный.
    a = str(a)
    return a

d = 5>10
print ("5>10", conv_type(d))
d = 5<10
print ("5<10", conv_type(d))
print()


#Задание 3
print()
print("Задание 3:")
print()

print ("Заполните список:")            #создание списка
array = []
i = 0
while len(array)<5:
    i = i+1
    print("Введите число №", i, "из 5:" )
    array.append(int(input()))


def raznost(n=[]):                    #Функция для вычисления разности, между минимальным и максимальным занчением списка
    w = max(n)-min(n)
    print("Разница между максимальным и минимальным значением списка: ", max(n), "-", min(n), "=", w)
    return w
    
raznost(array)
