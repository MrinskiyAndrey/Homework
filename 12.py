text = input('Введите символы: \n# = 5 \nO = 3 \nX = 1 \n! = -1 \n!! = -3 \n!!! = -5 \n')

def cryptography(L):
    symbols = {'#': 5, 'O': 3, 'X': 1, '!': -1, '!!': -3, '!!!': -5,}
    result = 0
    for list in L:
        for i in list:
            result += symbols.get(i)
            if result < 0:
                result = 0
    return result


print()
print('Резултат вычислений:')
print(cryptography(text))
