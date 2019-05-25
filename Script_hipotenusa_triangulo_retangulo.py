import math
catetooposto=int(input('digite o cateto oposto:'))
catetoadjacente=int(input('Digite o cateto adjacente:'))
hipotenusa=math.hypot(catetooposto,catetoadjacente)
print('A hipotenusa de {} e {} é:{}'.format(catetooposto,catetoadjacente,hipotenusa))