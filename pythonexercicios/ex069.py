condicao = 0
cont = 0
contm = 0
contf = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while True:
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).upper()[0]
        if idade >= 18:
            cont += 1
        if sexo == 'M':
            contm += 1
        if sexo == 'F' and idade < 20:
            contf += 1
        if sexo == 'M' or sexo == 'F':
            break
    condicao = str(input('Quer continuar[S/N] ')).upper()
    if condicao == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos: {cont}
Ao todo temos {contm} homens cadastrados.
E temos {contf} mulhres com menos de 20 anos.''')













