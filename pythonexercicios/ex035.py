a = float(input('Digite o valor A da reta: '))
b = float(input('Digite o valor B da reta: '))
c = float(input('Digite o valor C da reta: '))
if a + b > c and a + c > b and c + b > a:
    print(f'Os valores {a}, {b}, {c} FORMAM uma TRIÂNGULO.')
else:
    print('Os valores acima não formam um triângulo')
