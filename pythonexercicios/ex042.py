l1 = float(input('Digite um valor para o lado A: '))
l2 = float(input('Digite um valor para o lado B: '))
l3 = float(input('Digite um valor para o lado C: '))

if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l2:
    print(f'Os Valores {l1}, {l2},{l3} formam um triângulo!')
    if l1 == l2 == l3:
        print('A forma do triângulo é EQUILÁTERO.')
    elif l1 != l2 != l3 != l1:
        print('A forma do triângulo é ESCALENO.')
    else:
        print('A forma fo triângulo é ISÓSCELES')
else:
    print(f'Os valores {l1}, {l2}, {l3}, não formam um triângulo.')

