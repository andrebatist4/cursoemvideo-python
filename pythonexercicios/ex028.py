from random import randint
n1 = int(input('Digite um número de 0 a 5: '))
n2 = randint(1, 5)
if n1 == n2:
    print('Parabéns você venceu!')
else:
    print('Você perdeu!')
print('---fim---')
