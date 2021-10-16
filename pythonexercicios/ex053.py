from unidecode import unidecode
f = str(input('Digite a frase ou palavra: ')).replace(' ','')
s = unidecode(f).upper()
inver = s[::-1].upper()

if s == inver:
    print(f'o inverso de {s}, é {inver}.\nA frase digitada é um Palíndromo')
else:
    print(f'O inverso de {s}, é {inver}.\nA frase digitada não é um Palíndromo')
