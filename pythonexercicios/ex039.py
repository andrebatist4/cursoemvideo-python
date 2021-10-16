from datetime import date
data = date.today().year #data do pc

ano = int(input('Digite o ano em que nasceu: '))
c1 = data - ano
c2 = c1 - 18
c3 = 18 - c1

print(f'Quem nasceu em {ano} tem {c1} em {data}')
if c1 < 18:
    print(f'Você ainda vai se alistar!!! \nFaltam {c3} ano(s).')
elif c1 > 18:
    print(f'O tempo para se alistar já foi excedido!!! \nJá se passou {c2} ano(s).')
elif c1 == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
