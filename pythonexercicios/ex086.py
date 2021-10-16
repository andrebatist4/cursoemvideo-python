matriz = [[], [], []]
for i in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para [{0}, {i}]: ')))
for i in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para [{1}, {i}]: ')))
for i in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para [{2}, {i}]: ')))
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[[l][c]] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]}]', end='')
    print()
