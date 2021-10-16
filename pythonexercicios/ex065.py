cont = 0
cont2 = 0
stop = 0
maior = 0
menor = 0
while stop != 'n':
    cont += 1
    n = int(input('Digite um número: '))
    cont2 += n
    stop = str(input('Quer continuar? [s/n] ')).lower().strip()[0]
    print('=-='*10)
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'A média entre todos os valores foi {cont2/cont:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
