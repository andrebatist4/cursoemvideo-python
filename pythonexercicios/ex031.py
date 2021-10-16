n = int(input('Qual a distância a ser percorrida em Km? '))
if n <= 200:
    print(f'O preço da viagem é de: {0.5 * n} R$')
else:
    print(f'O preço da viagem é de: {0.45 * n} R$')
