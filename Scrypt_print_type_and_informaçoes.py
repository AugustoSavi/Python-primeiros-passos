def Verefica():
    var = input('digite algo:')
    print(type(var))
    print('Variavel é numerico?{}'.format(var.isnumeric()))
    print('Variavel é Alphanumerico?{}'.format(var.isalnum()))
    print('Variavel é Alpha?{}'.format(var.isalpha()))
    print('Variavel é espaço?{}'.format(var.isspace()))
    s = input('deseja continuar? 1-sim 0-não:')

    if s==1 :
        Verefica()
    else :
        StopIteration

pass

Verefica()

