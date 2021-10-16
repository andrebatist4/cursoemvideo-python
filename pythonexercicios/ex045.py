import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
print('\033[32;40mVamos jogar, Jokenpô!\033[m')
print('-=' * 11)
print('''\033[32;40m[ 0 ] para PEDRA\033[m
\033[32;40m[ 1 ] para PAPEL\033[m
\033[32;40m[ 2 ] para TESOURA\033[m''')
jogador = int(input('\033[32;40m Qual sua jogada?\033[m '))
print('-=' * 11)
print('\033[31mJO\033[m')
sleep(1)
print('\033[31mKEN\033[m')
sleep(1)
print('\033[31mPÔ\033[m')
print('-=' * 11)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if pc == 0:
   if jogador == 0:
       print('EMPATE')
   elif jogador == 1:
       print('JOGADOR VENCEU')
   elif jogador == 2:
       print('JOGADOR VENCEU')
   else:
       print('JOGADA INVÁLIDA!')

elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
