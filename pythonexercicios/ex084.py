lista = list()
dado = list()
cont = menor = maior = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    cont += 1
    sair = ' '
    while sair not in 'SN':
        sair = input('Quer continuar? ').upper()[0]
    if sair == 'N':
        break

print(f'Foram cadastrados no total {cont} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}], ', end='')
print()
print(f'O menor peso foi de {menor}. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
