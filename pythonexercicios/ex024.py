city = input('Digite o nome de uma cidade: ').upper().strip()
comando = city.find('SANTO')
if comando == 0:
    print(f'{city} começa com Santo')
else:
    print(f'{city} não tem Santo')
