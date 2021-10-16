palavras = ('abacate', 'abacaxi', 'suco', 'melancia', 'limão', 'manga',
            'pastel', 'pizza', 'chocolate', 'pao')
for i in palavras:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
