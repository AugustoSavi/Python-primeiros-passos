import random
while True:
    numr=random.randint(0,5)

    numusu=int(input('Tente acertar o numero,ele está entre 0 e 5:'))

    if numusu==numr:
        print('Parabéns você venceu!!')
    else: print('Você errou!!!')
    print('Numero Sorteado:{}\n'.format(numr))