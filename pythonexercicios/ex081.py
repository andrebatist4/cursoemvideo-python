lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).upper()[0]
    if sair == 'N':
        break
print('-=' * 30)
print(f'No total foram digitados {len(lista)} valores')
print(f'A lista de valores em ordem decrescente é {sorted(lista, reverse=True)}')
if 5 not in lista:
    print('O valor 5 não foi digitado !')
else:
    print(f'O valor 5 foi digitado, e está na posição ', end='')
for i, v in enumerate(lista):
    if 5 == v:
        print(f'{i}...', end='')
print()


