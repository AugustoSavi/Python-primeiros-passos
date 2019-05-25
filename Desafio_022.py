nome=input('Digite seu nome Completo:')

dividido=nome.strip().split()
print('dividido:{}'.format(dividido))

quantdenome=len(dividido)
print('quantidade de palavras:{}'.format(quantdenome))

soma=0
print('valor soma:{}'.format(soma))

quantdeletra=len(dividido[0])+len(dividido[1])

print('Todaas maiusculas:{}'.format(nome.upper()))
print('todas minusculas:{}'.format(nome.lower()))
print('quant de letras sem consideras espaços:{}'.format(quantdeletra))
print('quantidade de letras no primeiro nome:{}'.format(len(dividido[0])))