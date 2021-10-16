cont = maior = menor = 0
valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posoção {i}: ')))
    '''if i == 0:
        maior = menor = valores[i]
    else:
        if valores[i] > maior:
            maior = valores[i]
        if valores[i] < menor:
            menor = valores[i]'''
maior = max(valores)
menor = min(valores)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for x, v in enumerate(valores):
    if v == maior:
        print(f'{x}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for x, v in enumerate(valores):
    if v == menor:
        print(f'{x}...', end='')
print()
