choise = ''
while choise != '1' or '2':
    choise = input('Если хотите зашифровать текст - нажмите 1\nЕсли хотите расшифровать тест - нажмите 2.\n')
    if choise == "1":
        text = input('Введите текст\n')
        break
    elif choise == "2":
        text = list(map(int,input('Введите кодировку через пробел \n').split()))
        break
    else:
        print("Некорректный ввод")



def coder(txt):
    
    code_list = [ ]         #объявление кодированого списка
    decode_string = ""     #объявление декодированной строки
    i=0                     #счетчик цикла
    
    if type (txt) == str:
        code_list.append(ord(txt[0]))   #добавление ascii кода, первого символа строки
        while i < (len(txt)-1):
            code_tmp_1 = (ord(txt[i+1]) - ord(txt[i])) #шифрование согласно заданию
            code_list.append(code_tmp_1) #добавление шифрованого кода
            i+=1
        return code_list


    if type (txt) == list:
            decode_string = decode_string+chr(txt[0])       #добавление первого символа строки
            while i < (len(txt)-1):
                code_tmp_2 = txt[i-1] + txt[i]  #дешифровка согласно заданию
                decode_string = decode_string + chr(code_tmp_2)  #добавление дешифрованого символа
                i+=1
            return decode_string
    
print(coder(text))

