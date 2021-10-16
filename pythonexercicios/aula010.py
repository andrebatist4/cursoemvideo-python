nome = str(input('Qual o seu nome? ')).strip()
if nome == 'ANDRÉ':
    print('Que nome lindo você tem!')
print(f'Bom dia {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS')
