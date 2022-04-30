print('Введите строку кириллицей :\n')
text = input().upper().split()

def func(t):
    glas = {'А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я'}
    soglas = {'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н', 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь'}
    str1 = []
    str2 = []
    for i in t:
        if i == glas:
            str1.append(i)
        elif i == soglas:
            str2.append(i)
        print('Гласные: \n', str1, '\nсогласные: \n', str2)

func(text)
