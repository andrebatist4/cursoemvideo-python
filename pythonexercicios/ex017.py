from math import hypot
catetoop = float(input('Digite o comprimento do cateto oposto: '))
catetoadj = float(input('Digite o comprimento do cateto adjacente: '))
calculo = hypot(catetoop, catetoadj)
print('O comprimento da hipotenusa é: {:.2f}'.format(calculo))
