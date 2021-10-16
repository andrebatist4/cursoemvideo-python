lista = []
notas = []
media = sair = 0
while True:
    n = str(input('Nome: '))
    lista.append(n)
    no1 = float(input('Nota 1: '))
    lista.append(no1)
    no2 = float(input('Nota 2: '))
    lista.append(no2)
    media = (no1 + no2) / 2
    lista.append(media)
    notas.append(lista[:])
    lista.clear()
    s = ' '
    while s not in 'SN':
        s = input('Quer continuar? [S/N] ').upper()[0]
    if s == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, l in enumerate(notas):
    print(f'{i:<4}{l[0]:<10}{l[3]:>7.1f} ')
while True:
    print('-='*35)
    sair = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if sair == 999:
        print('FINALIZANDO...')
        break
    if sair <= len(notas) - 1:
        print(f'Notas de {notas[sair][0]} são {notas[sair][1:3]}')
print('<<< VOLTE SEMPRE >>>')
