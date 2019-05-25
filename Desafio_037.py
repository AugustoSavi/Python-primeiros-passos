while True:
    num = int(input('Digite o valor:'))
    esc = int(input('Escolha a base para conversão,1-binario,2-octal,3-hexadecimal:'))

    if esc== 1:
        print('{} em binario:{}'.format(num,bin(num)))
    elif esc== 2:
        print('{} em octal:{}'.format(num,oct(num)))
    elif esc == 3:
        print('{} em hexadecimal:{}'.format(num,hex(num)))
    else:print('Essa opção não existe!!!')