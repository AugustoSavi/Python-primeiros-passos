cont = int(0)
maior = int(0)
string3=''
while (True):

    string1 = str(input("informe a frase:"))

    string2 = str(input("informe a segunda frase:"))

    if (len(string1) > maior):
        maior = len(string1)

    if (len(string2) > maior):
        maior = len(string2)

    string3 = string3 + string1 + string2
    cont = cont + 2

    if (string1 == string2):
        break

print('maior:' + str(maior))
print('string concatenada:' + str(string3))
print('frases contadas:' + str(cont))
