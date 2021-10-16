cont = 0
s = 0
print('[Digite [999] para parar!')
while True:
    p = int(input('Digite um valor: '))
    if p == 999:
        break
    cont += 1
    s += p
print(f'No total foram digitados {cont} valores, e a soma de todos é de {s} ')
