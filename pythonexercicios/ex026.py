frase = str(input('Digite uma frase: ').upper().strip())
print(f'Na frase aparece {frase.count("A")} letras A')
print(f'A primera vez que o "A" aparece é na posição: {frase.find("A")+1}')
print(f'A última vez que o "A" aperece é na posição {frase.rfind("A")+1}')




