while True:
    dis=int(input('Informe a distancia:'))

    if dis<=200:
        print('A passagem vai custar:R${}!'.format(dis*0.50))
    else:print('A passagem vai custar:R${}'.format(dis*0.45))