while True:
    idade =int(input('Digite seu ano de nascimento:'))
    idade=2018-idade
    print('Idade:{}'.format(idade))

    if idade <=9 : print('Junior')

    if idade > 9 and idade <=14: print('Infantil')

    if idade > 14 and idade <= 19 :print('Junior')

    if idade>19 and  idade<=20:print('Sênior')

    if idade>20:print('Master')