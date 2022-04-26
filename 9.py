
 
def translate():
    text = []
    text = str(input('Введите текст: ')).lower()
    print(text)
    morse = []
    for string in text:
        if string == 'a':
            morse_code = (' .- ')
            print(morse_code)
            morse.append(morse_code)
        elif string == 'b':
            morse_code = (' -... ')
            print(' -... ')
            morse.append(morse_code)
        elif string == 'c':
            morse_code = (' -.-. ')
            print(' -.-. ')
            morse.append(morse_code)
        elif string == 'd': 
            morse_code = (' -.. ')
            print(' -.. ')
            morse.append(morse_code)
        elif string == 'e':
            morse_code = (' . ')
            print(' . ')
            morse.append(morse_code)
        elif string == 'f':
            morse_code = (' ..-. ')
            print(' ..-. ')
            morse.append(morse_code)
        elif string == 'g':
            morse_code = (' --. ')
            print(' --. ')
            morse.append(morse_code)
        elif string == 'h':
            morse_code = (' .... ')
            print(' .... ')
            morse.append(morse_code)
        elif string == 'i':
            morse_code = (' .. ')
            print(' .. ')
            morse.append(morse_code)
        elif string == 'j':
            morse_code = (' .--- ')
            print(' .--- ')
            morse.append(morse_code)
        elif string == 'k':
            morse_code = (' -.- ')
            print(' -.- ')
            morse.append(morse_code)
        elif string == 'l':
            morse_code = (' .-.. ')
            print(' .-.. ')
            morse.append(morse_code)
        elif string == 'm':
            morse_code = (' -- ')
            print(' -- ')
            morse.append(morse_code)
        elif string == 'n':
            morse_code = (' -. ')
            print(' -. ')
            morse.append(morse_code)
        elif string == 'o':
            morse_code = (' --- ')
            print(' --- ')
            morse.append(morse_code)
        elif string == 'p':
            morse_code = (' .--. ')
            print(' .--. ')
            morse.append(morse_code)
        elif string == 'q':
            morse_code = (' --.- ')
            print(' --.- ')
            morse.append(morse_code)
        elif string == 'r':
            morse_code = (' .-. ')
            print(' .-. ')
            morse.append(morse_code)
        elif string == 's':
            morse_code = (' ... ')
            print(' ... ')
            morse.append(morse_code)
        elif string == 't':
            morse_code = (' - ')
            print(' - ')
            morse.append(morse_code)
        elif string == 'u':
            morse_code = (' ..- ')
            print(' ..- ')
            morse.append(morse_code)
        elif string == 'v':
            morse_code = (' ...- ')
            print(' ...- ')
            morse.append(morse_code)
        elif string == 'w':
            morse_code = (' .-- ')
            print(' .-- ')
            morse.append(morse_code)
        elif string == 'x':
            morse_code = (' -..- ')
            print(' -..- ')
            morse.append(morse_code)
        elif string == 'y':
            morse_code = (' -.-- ')
            print(' -.-- ')
            morse.append(morse_code)
        elif string == 'z':
            morse_code = (' --.. ')
            print(' --.. ')
            morse.append(morse_code)
        elif string == '1':
            morse_code = (' .---- ')
            print(' .---- ')
            morse.append(morse_code)
        elif string == '2':
            morse_code = (' ..--- ')
            print(' ..--- ')
            morse.append(morse_code)
        elif string == '3':
            morse_code = (' ...-- ')
            print(' ...-- ')
            morse.append(morse_code)
        elif string == '4':
            morse_code = (' ....- ')
            print(' ....- ')
            morse.append(morse_code)
        elif string == '5':
            morse_code = (' ..... ')
            print(' ..... ')
            morse.append(morse_code)
        elif string == '6':
            morse_code = (' -.... ')
            print(' -....')
            morse.append(morse_code)
        elif string == '7':
            morse_code = (' --... ')
            print(' --... ')
            morse.append(morse_code)
        elif string == '8':
            morse_code = (' ---.. ')
            print(' ---..')
            morse.append(morse_code)
        elif string == '9':
            morse_code = (' ----. ')
            print(' ----. ')
            morse.append(morse_code)
        elif string == '0':
            morse_code = (' ----- ')
            print(' ----- ')
            morse.append(morse_code)
        elif string == '&':
            morse_code = (' .-... ')
            print(' .-... ')
            morse.append(morse_code)
        elif string == " ' ":
            morse_code = (' .----. ')
            print(' .----. ')
            morse.append(morse_code)
        elif string == '@':
            morse_code = (' .--.-. ')
            print(' .--.-. ')
            morse.append(morse_code)
        elif string == ')':
            morse_code = (' -.--.- ')
            print(' -.--.- ')
            morse.append(morse_code)
        elif string == '(':
            morse_code = (' -.--. ')
            print(' -.--.')
            morse.append(morse_code)
        elif string == ':':
            morse_code = (' ---... ')
            print(' ---... ')
            morse.append(morse_code)
        elif string == ',':
            morse_code = (' --..-- ')
            print(' --..-- ')
            morse.append(morse_code)
        elif string == '=':
            morse_code = (' -...- ')
            print(' -...- ')
            morse.append(morse_code)
        elif string == '!':
            morse_code = (' -.-.-- ')
            print(' -.-.-- ')
            morse.append(morse_code)
        elif string == '.':
            morse_code = (' .-.-.- ')
            print(' .-.-.- ')
            morse.append(morse_code)
        elif string == '-':
            morse_code = (' -....- ')
            print(' -....- ')
            morse.append(morse_code)
        elif string == '+':
            morse_code = (' .-.-. ')
            print(' .-.-. ')
            morse.append(morse_code)
        elif string == '"':
            morse_code = (' .-..-. ')
            print(' .-..-. ')
            morse.append(morse_code)
        elif string == '?':
            morse_code = (' ..--.. ')
            print(' ..--.. ')
            morse.append(morse_code)
        elif string == '/':
            morse_code = (' -..-. ')
            print(' -..-. ')
            morse.append(morse_code)
        elif string == ' ':
            morse_code = ('   ')
            print('   ')
            morse.append(morse_code)
 
 
    morse = ''.join(morse)
    print('Одной строкой: ', morse)
 


translate()


