from random import randint
from time import sleep
print('-'*30)
print('     JOGA NA MEGA SENA     ')
print('-'*30)

lista = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for j in range(quant):
    lista2 = []
    for c in range(1, 7):
        lista2.append(randint(1, 60))
    lista2.sort()
    lista.append(lista2)
print(F'-=-=-= SORTEANDO {quant} JOGOS -=-=-=')
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '< BOA SORTE! >', '-='*5)
