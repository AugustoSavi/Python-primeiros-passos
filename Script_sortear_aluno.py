import random
vetor=[]
n=0
while n<4:
    vetor.append(input('digite o nome[{}]:'.format(n)))
    n+=1

sorteado=random.randint(0,3)
print('O numero sorteado é:{}'.format(sorteado))
print('O aluno sorteado é:{}'.format(vetor[sorteado]))