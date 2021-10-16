nome = input('Digite seu nome: ').upper().strip()
comando = nome.find('SILVA')
if comando == -1:
    print(f'{nome} não tem SILVA no nome.')
else:
    print(f'{nome} tem SILVA no nome.')

# nome = str(input('Qual o seu nome completo? ')).strip()
#print(f'Seu nome tem silva? {"silva" in nome.lower()}')
