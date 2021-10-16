from random import randint
result = 0
pi2 = 0
cont = 0
p1 = 0
print('-='*25)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*25)
while True:
    jog = int(input('Digite um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P/I] ')).upper()[0]
    pc = randint(1, 10)
    s = jog + pc
    resto = s % 2
    if resto == 0:
        result = 'p'
        pi2 = 'PAR'
    else:
        result = 'i'
        pi2 = 'ÍMPAR'

    if result == pi:
        p1 = 'VENCEU'
        cont += 1
    if result != pi:
        p1 = 'PERDEU'

    print(f'Você jogou {jog} e o computador {pc}. Total de {s} deu {pi2}')
    print('-'*25)
    print(f'Você {p1}')
    if result != pi:
        break
    if p1 == 'VENCEU':
        print('Vamos jogar novamente...')
    print('-' * 25)

print('-='*25)
print(f'GAME OVER! Você venceu {cont} vezes.')










