n = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
print('- 1 para binário')
print('- 2 para octal')
print('- 3 para hexadecimal')
base = int(input('Digite o valor correspondente (ex: 1): '))

if base == 1:
    print(bin(n)[2:])
elif base == 2:
    print(oct(n)[2:])
elif base == 3:
    print(hex(n)[2:])
