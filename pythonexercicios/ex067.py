print('---------TABUADA---------\nDigite número negativo para sair!')
print('-='*17)
while True:
    n = int(input('Digite um valor: '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{i} * {n} = {i*n}')
