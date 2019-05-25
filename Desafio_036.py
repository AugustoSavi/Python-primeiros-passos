while True:
    casa=float(input('Digite o valor da casa:'))
    sal=float(input(('digite o valor do deu salario:')))
    anos=int(input('Em quantos anos vc quer pagar a casa?:'))
    pres= casa/(anos*12)
    print('Prestação:{}'.format(pres))
    if (pres>(sal*0.30)):
        print('O valor da prestação ficara em:{}'.format(casa/(anos*12)))
    else:print('As parcelas execedem o 30% do seu salario!!')
