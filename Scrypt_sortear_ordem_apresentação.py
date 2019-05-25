import random
vetor=[]
n=0
while n<4:
    vetor.append(input('digite o nome[{}]:'.format(n)))
    n+=1

sorteado=[]

while len(sorteado)!=4:
    r = random.randint(0,3)
    if r not in sorteado:
        sorteado.append(r)

print('first:{}\nsegundo:{}\nterceiro:{}\nquarto:{}'.format(vetor[sorteado[0]], vetor[sorteado[1]], vetor[sorteado[2]], vetor[sorteado[3]]))

