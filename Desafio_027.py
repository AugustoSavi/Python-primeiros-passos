while True:
    nome = input('\nDigite o nome:')

    div=nome.split()
    print('Div:{}'.format(div))

    tam = len(div)
    print('Div:{}'.format(tam))

    print('Primeiro nome:{}'.format(div[0]))
    print('Ultimo nome:{}'.format(div[tam-1]))