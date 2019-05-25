lista=[0,1,2,3,4,5,6,7,8,9,10]
num = int(input('digite um numero:'))

for n in lista :
    print('{}X{}={}'.format(num, n,(num*n)))
else:
    print('Tabuada Concluida!')