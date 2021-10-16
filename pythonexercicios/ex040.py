n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
result = (n1 + n2) / 2
if result < 5.0:
    print(f'Reprovado!Sua nota foi {result}, e não atingiu a nota miníma de 5.0.')
elif result < 6.9:
    print(f'Recuperação! Sua nota foi {result}, e não atingiu a média 7.0')
elif result >= 7.0:
    print(f'Parabéns, você aprovado!Sua nota {result}.')
