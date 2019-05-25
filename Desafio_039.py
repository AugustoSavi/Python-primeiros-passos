idade = int(input('Informe o ano de nascimento:'))
print('idade:{}'.format(2018-idade))
if (2018-idade)<18:
    print('Vc ainda não precisa se apresentar')
    print('Falta{} Anos para vc poder se alistar.'.format(18-(2018-idade)))
elif (2018-idade)==18:print('Esta na hora de se alistar')
elif(2018-idade)>18:
    print('Já passou o tempo de se alistar')
    print('Passou {} Anos do tempo de se alistar'.format((2018-idade)-18))