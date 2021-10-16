n = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))

print(f'Você digitou os valores {n}')
cont = n.count(9)
if cont != 0:
    print(f'O valor 9 apareceu {cont} vezes')
else:
    print('O valor 9 apareceu 0 vezes')

if 3 in n:
    print(f'O valor 3 foi digitado na posição {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares digitados foram ', end='')
for i in n:
    if i % 2 == 0:
        print(i, end=' ')








