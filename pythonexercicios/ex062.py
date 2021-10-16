t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        c += 1
        t += r
        print(f'{t} → ', end='')
    print('PAUSA')
    mais = int(input(f'Quer mostrar mais alguns termos?  ' ))
print('FIM')
