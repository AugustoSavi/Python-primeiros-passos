while True:
    sal=float(input('Digite o salario:'))
    if sal>1250:
        print('O aumento é 10% = R$:{} e seu salario passa a ser:R${}'.format((sal*0.10), sal+(sal*0.10)))
    else:
        print('O aumento é 15% = R$:{} e seu salario passa a ser:R${}'.format((sal * 0.15), sal + (sal * 0.15)))