lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    s = ' '
    while s not in 'SN':
        s = input('Quer continuar? [S/N] ').upper()[0]
    lista.append(n)

    if n % 2 == 0:
        p = n
        par.append(p)
    else:
        i = n
        impar.append(i)
    if s == 'N':
        break
'''for i, v in enumerate(n):
       if v % 2 == 0:
          par.append(v)
       elif v % 2 == 1:
            impar.append(v)'''

print('-=' * 25)
print(f'Lista dos valores: {lista}')
print(f'Lista dos valores pares: {par}')
print(f'Lista dos valores ímpares: {impar}')
