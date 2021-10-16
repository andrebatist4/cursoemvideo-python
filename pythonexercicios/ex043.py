print('IMC')
peso = float(input('Digite o peso (ex: 55.6): '))
alt = float(input('Digite a altura (ex: 1.70): '))
conta = peso / (alt ** 2)

print(f'O seu índice de massa corpórea é {conta:.1f}.')

if conta < 18.5:
    print('\033[31mAbaixo do peso! \033[m')
elif conta < 25:
    print('\033[34mPeso ideal! \033[m')
elif conta < 30:
    print('\033[33mSobrepeso! \033[m')
elif conta < 40:
    print('\033[35mObesidade!\033[m')
elif conta >= 40:
    print('\033[31mObesidade mórbida! \033[m')
