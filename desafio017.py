# faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print(f'A hipotenusa vai medir {hypot(ca, co):.2f}')
# Tambem pode usar sem necessidade de criar variavel para receber o valor de hip
print('A hipotenusa vai medir {}'.format(hypot(ca,co)))
# mas tambem pode criar usar uma variavel que recebe o valor da hip


