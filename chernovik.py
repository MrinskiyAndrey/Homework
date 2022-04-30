
print('Введите строку кириллицей :\n')
text = str(input().upper().split())

def func(t):
    glas = 'АЕЁИОУЫЭЮЯ'
    soglas = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ'
    str1 = []
    str2 = []
    for i in glas:
        if t.find(i):
             str1.append(i)
    
    for i in soglas:
        if t.find(i):
             str2.append(i)
    print('Гласные: \n', str1, '\nсогласные: \n', str2)
    
func(text)
