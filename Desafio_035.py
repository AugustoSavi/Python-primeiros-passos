while True:
    a=int(input('Digite o valor:'))
    b=int(input('Digite o valor:'))
    c=int(input('Digite o valor:'))

    if (a<(b+c)) & (b<(a+c)) & (c<(a+b)):
        print('É possivel formar um triangulo!!!')
    else:print('Não é possivel formar um triangulo!!!\n')
    