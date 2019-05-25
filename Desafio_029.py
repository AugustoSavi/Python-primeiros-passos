while True:
    velocidade= int(input('Velocidade do carro:'))

    if velocidade>80:
        print('Você foi Multado e o valor da multa é:R${}!!'.format((velocidade-80)*7))
    else:print('Velocidade aceita!!\n')