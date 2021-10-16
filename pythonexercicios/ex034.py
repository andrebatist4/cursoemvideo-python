s = float(input('Digite o salário do funcionário: '))
if s > 1250.0:
    print(f'O reajuste salárial é de {( s / 100) * 10 + s}')
else:
    print(f'O ajuste salárial é de {(s / 100) * 15 + s}')
