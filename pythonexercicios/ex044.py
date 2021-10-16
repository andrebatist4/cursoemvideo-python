preco = float(input('Digite o preço das compras: '))
print('digite: \n1 - pagamento à vista dinheiro/cheque.')
print('2 - pagamento à vista no cartão.')
print('3 - pagamento em até 2x no cartão.')
print('4 - pagamento em até 3 x ou mais no cartão.')
pag = int(input('Qual a forma de pagamento?(ex:1) '))

if pag == 1:
    print(f'O valor {preco} reais, teve um desconto de 10% e ficou por {preco - (preco * 0.1)} reais')
elif pag == 2:
    print(f'O preço {preco} reais, teve um desconto de 5% e ficou por {preco - (preco * 0.05)} reais')
    parc = int(input('Em quantas vezes? '))
    print(f'Sua compra será parcelada em {parc}x de {(preco - (preco * 0.05)) / parc}')
elif pag == 3:
    print(f'O preço não foi alterado')
elif pag == 4:
    print(f'O preço {preco} reais, teve um acrescimo de 20% e ficou por {preco + (preco * 0.2)} reais')
    parc = int(input('Em quantas vezes? '))
    print(f'Sua compra será parcelada em {parc}x de {(preco + (preco * 0.2)) / parc}')
