matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = par = col = 0
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c][i] = int(input(f'Digite um valor [{c}] [{i}]: '))
print('-='*30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c] [i]:^5}]', end='')
        if matriz[c][i] % 2 == 0:
            par += matriz[c][i]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {par}')
for c in range(0, 3):
    col += matriz[c][2]
print(f'A soma dos valores pares da terceira coluna é {col}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c]:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')
