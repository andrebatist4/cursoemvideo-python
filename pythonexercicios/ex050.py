s = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite o valor: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'Você informou {cont} número(s) PARES e a soma foi {s}')
