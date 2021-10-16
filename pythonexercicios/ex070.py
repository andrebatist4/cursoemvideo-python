soma = cont = cont2 = menor = nome = 0
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
    cont2 += 1
    n = str(input('Nome do produto: '))
    v = float(input('Valor do produto: '))
    s = ' '
    while s not in 'SN':
        s = str(input('Quer continuar? [S/N] ')).upper()[0]
    if s == 'N':
        break
    soma += v
    if v >= 1000:
        cont += 1
    if cont2 == 1:
        menor = v
    else:
        if v < menor:
            menor = v
            nome = n
print(f'''O total da compra foi R${soma}
Temos {cont} produtos custando mais de R$1000.00
O produto mais barato foi "{nome}" que custa R${menor}''')
