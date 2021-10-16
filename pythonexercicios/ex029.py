n = float(input('Qual a velocidade do carro? '))
if n > 80:
    print('Você foi multado!')
    print(f'E o valor da multa é de: {(n - 80) * 7} R$')
else:
    print('O limite não foi excedido')

