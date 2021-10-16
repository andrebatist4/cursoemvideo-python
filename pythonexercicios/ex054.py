from datetime import date
cont2 = 0
cont = 0
ano = date.today().year
for i in range(1, 8):
    n = int(input(f'Em que ano a {i}ª pesooa nasceu? '))
    r = ano - n
    if r >= 21:
        cont += 1
    elif r < 21:
        cont2 += 1
print(f'Ao todo tivemos {cont} maiores de idade\nE também {cont2} menores de idade. ')
