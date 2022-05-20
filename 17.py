#Задание 17:
'''Имеется строк из символов в нижнем регистре ascii[["a".."z"]].
Нужно сократить строку следующим образом: берется пара соседних символов и если они одинаковы, то они удаляются.
Например aab должно превратится в b. Нужно удалить как можно больше символов.
Если результирующая строка пустая, нужно вернуть "Empty String"'''


text = input("Введите строку\n").lower()

def doubledelete (string):
    string += ' ' #Добавление пробела в конец для избегания 'out of range'
    result = ''   #Объявление выходной строки
    for i in range(len(string)-1):
        if string[i+1] != string[i]:
            result += string[i]
        else:
            i+=1
    if result == '':
        result += 'Empty String'
    return result

print(doubledelete(text))

