numero = input('Escreva um número de 0 a 9999: ')
qtnumero = len(numero)

if qtnumero == 4:
 print(f'Unidade: {numero[3]}')
 print(f'Dezena: {numero[2]}')
 print(f'Centena: {numero[1]}')
 print(f'Milhares: {numero[0]}')

if qtnumero == 3:
     print(f'Unidade: {numero[2]}')
     print(f'Dezena: {numero[1]}')
     print(f'Centena: {numero[0]}')

if qtnumero == 2:
    print(f'Unidade: {numero[1]}')
    print(f'Dezena: {numero[0]}')

if qtnumero == 1:
    print(f'Unidade: {numero[0]}')
    












