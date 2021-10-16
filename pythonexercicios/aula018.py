teste = list()
teste.append('André')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['André', 20], ['Maria', 19], ['João', 22], ['Manoel', 33]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
