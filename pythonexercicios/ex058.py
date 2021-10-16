from random import randint
print('---------- Mini game ----------')
print(' ')
jog = int(input('Digite um nùmero de 0 a 10: '))
pc = randint(0, 10)
cont = +1
while pc != jog:
    cont += 1
    jog = int(input('Digite um valor de 0 a 10: '))
print(f'Exatamente eu pensei no número [{pc}]\n\033[34mVocê advinhou!!!\033[m \nE precisou de {cont} palpite(s) para acertar!')
