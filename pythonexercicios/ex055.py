maior = 0
menor = 0
for i in range(1, 6):
    p = float(input(f'Peso da {i}ª pessoa: '))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O maior peso lido foi de {maior}Kg')
print(f'o menor peso lido foi de {menor}kg')
