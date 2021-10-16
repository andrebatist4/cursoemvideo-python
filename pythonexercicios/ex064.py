print('Para PARAR digite [999]!')
tot = 0
n = 0
c = 0
while n != 999:
    c += 1
    n = int(input('Digite valores: '))
    if n != 999:
        tot += n
print('-='*10)
print(f'No total foram digitados {c - 1} números e a soma foi {tot}. ')

