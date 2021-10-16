maior = 0
menu = 0

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

while menu != 5:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    menu = int(input('Digite a opção desejada: '))
    if menu == 1:
        s = n1 + n2
        print(f'{n1} + {n2} = {s}')

    if menu == 2:
        m = n1 * n2
        print(f'{n1} * {n2} = {m}')

    if menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print(f'O maior número é {maior}')

    print('-=' * 15)

    if menu == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))

    if menu == 5:
        print('\033[31mEncerrado!\033[m')


















