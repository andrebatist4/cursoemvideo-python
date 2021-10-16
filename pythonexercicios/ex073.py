print('-='*10)
lista = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória''Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('-='*10)
print(f'Os 5 primeiros são {lista[0:5]}')
print('-='*10)
print(f'Os 4 últimos são {lista[-4:]}')
print('-='*10)
print(f'Time em ordem alfabética: {sorted(lista)}')
print('-='*10)
print(f'O chapecoense está na {lista.index("Chapecoense")+1} posição')
