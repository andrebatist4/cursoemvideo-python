print('ex01:')
for c in range (1, 6):
    print('Oi')
print('FIM')

print('-=' *10)
print('ex02')
for c in range(0, 7, 2):#PULA DUAS CASAS(2)
    print(c)
print('FIM')

print('-=' *10)
print('ex03')
i = int(input('Início: '))
f = int(input('fim:'))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')
print('-=' *10)

print('-=' *10)
print('ex04')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório de todos os valres foi {s}')
