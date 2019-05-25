frase='Curso em video de Python'

#conta a quantidade de caracteres
print(len(frase))

#troca o primeiro argumento pelo segundo
print(frase.replace('Python','Android'))

#retorna a posição que começa(retorna -1 se não encontrar a palavra)
print(frase.find('Python'))

#retorna um bool
print('em' in frase)

#coloca tudo em caixa auta
print(frase.upper())

#coloca tudo em caixa baixa
print(frase.lower())

#deixa somente a primeira letra em maiusculo
print(frase.capitalize())

#coloca toda primeira letra de uma palavra em maiuscula
print(frase.title())

#remove os espaços do começo e do fim da cadeia
print(frase.strip())

#remove os espaços do fim da cadeia
print(frase.rstrip())

#remove os espaços do começo da cadeia
print(frase.lstrip())

#divede as palavras em seus espaços
print(frase.split())
dividido =frase.split()
print(dividido[0])

#pega a lista é une com o caracter escolhido
print('-'.join(frase))

#Joga a frase no meio do caracter escolhido
print(' {:=^50} '.format(' Adivinhe a palavra ! '))