t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
s = t + (11 - 1) * r
for i in range(t, s, r):
    print(f'{i} ',end='→ ')
print('ACABOU')


