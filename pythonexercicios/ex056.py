maiorid = 0
menor = 0
media = 0
nomeid = ''
cont = 0

for i in range(1, 5):
      print(f'----- {i}ª PESSOA -----')
      nome = str(input('Nome: '))
      idade = int(input('Idade: '))
      sexo = str(input('Sexo [M/F]: '.upper()))
      media += idade
      if i == 1 and sexo and 'Mm':
            maiorid = idade
            nomeid = nome
      if sexo in 'Mm' and idade > maiorid:
            maiorid = idade
            nomeid = nome
      if sexo in 'F' and idade < 20:
            cont += 1

print(f'A média de idade do grupo é de {media / 4} anos.')
print(f'O homem mais velho tem {maiorid} e se chama {nomeid}.')
print(f'Ao todo são {cont} mulher(es) com menos de 20 anos.')
