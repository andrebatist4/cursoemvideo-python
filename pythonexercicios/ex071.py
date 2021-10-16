print('========= BANCO CEV ==========')
print('='*30)
n = int(input('Que valor quer sacar? R$ '))

while True:
    if n != 0:
        div1 = n // 50
        s1 = n % 50
        div2 = s1 // 20
        s2 = s1 % 20
        div3 = s2 // 10
        s3 = s2 % 10
        div4 = n
        if div1 != 0:
            print(f'Total de {div1} cédulas de R$50')
        if div2 != 0:
            print(f'Total de {div2} cédulas de R$20')
        if div3 != 0:
            print(f'Total de {div3} cédulas de R$10')
        if div4 != 0:
            print(f'Total de {div4} cédulas de R$1')
        if div1 or div2 or div3 == 0:
            break
        if div4 == n:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
