# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

# Para formar triangulo, e que a soma das medidas de quaisquer dois lados deve ser sempre maior que a medida do terceiro lado

r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'As retas {r1}, {r2} e {r3} podem formar um triangulo!')
else:
    print(f'As retas {r1}, {r2} e {r3} nao  podem formar um triangulo!')
