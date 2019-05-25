while True:
    n1=float(input('Digite o valor da primeira nota:'))

    n2=float(input('Digite o valor da segunda nota:'))

    if ((n1+n2)/2)<5:print('Reprovado,nota:{}'.format((n2+n1)/2))

    elif ((n1+n2)/2)>=5.0:
        if ((n1 + n2) / 2) <= 6.9: print('Recuperação,nota:{}'.format(((n1+n2))/2))

    elif (n1+n2)/2>7.0:print('Aprovado,nota:{}'.format((n2+n1)/2))