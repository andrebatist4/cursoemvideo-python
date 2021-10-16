from math import tan, cos, sin, trunc, radians
angulo = float(input('Digite o ângulo desejado: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'Os valores do ângulo {trunc(angulo)} graus, são: \nseno: {seno:.2f} \ncosseno: {cosseno:.2f} \ntangent: {tangente:.2f}')
