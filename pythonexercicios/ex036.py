from math import ceil
casa = float(input('Qual o valor do imóvel? '))
salario = float(input('Valor do sálario atual do comprador: '))
anos = float(input('Digite em quantos anos pretender pagar: '))

#minimo a considerar:
c1 = salario * 0.3 #sálario
c2 = (casa / c1) / 12
c3 = ceil(c2) #anos arrendodado, resul c2
c4 = c3 * 12 #quantidade de parcelas
c5 = casa / c4

#resultado
c7 = casa / (anos * 12)

if c3 <= anos:
    print(f'\033[34mO comprador irá pagar {c7:.2f}\033[m')
else:
    print('\033[31mEmpréstimo negado a parcela excedeu 30% do sálario !!!\033[m')
    print(f'\033[34mMas conseguimos em {c3} anos, no valor da parcela de {c5:.2f}.\033[m')


