n1 = int(input('Digite um número entre 0 e 20: '))
while n1 > 20 or n1 < 0:
    n1 = int(input('Tente novamente. Digite um número entre 0 e 20: '))

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')

print(f'Você digitou o número {num[n1]}')
