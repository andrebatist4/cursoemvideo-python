valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    sair = ' '
    while sair not in 'SN':
        sair = input('Quer continuar? [S/N] ').upper()[0]
    if sair == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
