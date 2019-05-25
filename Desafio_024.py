while True:
    nome=input('digite o nome da cidade:')

    divisao=nome.upper().split()

    print(divisao)

    if 'SANTO' in divisao[0]:
        print('Contem!!')
    else:print('Não Contem!!')