while True:
    num = input('digite um numero:')

    tam=len(num)

    if tam ==1:
        print('unidade:{}'.format(num[0]))

    if tam==2:
        print('unidade:{}'.format(num[1]))
        print('dezena:{}'.format(num[0]))

    if tam==3:
        print('unidade:{}'.format(num[2]))
        print('dezena:{}'.format(num[1]))
        print('centena:{}'.format(num[0]))

    if tam==4:
        print('unidade:{}'.format(num[3]))
        print('dezena:{}'.format(num[2]))
        print('centena:{}'.format(num[1]))
        print('milhar:{}'.format(num[0]))