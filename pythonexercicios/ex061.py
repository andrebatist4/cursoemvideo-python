print('Gerador de PA')
print('-='*10)
t = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 1
pt = t
while c <= 10:
    c += 1
    pt += r
    print(f'{pt} → ', end='')
print('Acabou!')



