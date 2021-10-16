lista = [[], []]
for i in range(1, 8):
    val = int(input(f'Digite o {i}o valor: '))
    if val % 2 == 0:
        lista[0].append(val)
    else:
        lista[1].append(val)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')
