from datetime import date
ano = int(input('Digite algum ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')