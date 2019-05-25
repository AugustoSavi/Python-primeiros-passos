reais=float(input('digite a quantidade de reais:'))
moeda=float(input('digite a cotação da moeda atualmente:'))
print('Com {} R$ você pode comprar: {:.2f} '.format(float(reais),float((reais/moeda))))