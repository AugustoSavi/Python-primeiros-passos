while True:
    num=[]
    for aux in range(3):
     num.append(int(input('Digite o numero {}:'.format(aux))))

    print('O maior numero:{}'.format(max(num)))
    print('O menor numero:{}'.format(min(num)))
