# faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math

angulo =int(input('Digite o angulo que voce deseja: '))
# tem que converte para radiano para fica correto
print(f'O angulo de {angulo} tem SENO de {math.sin((math.radians(angulo))):.2f}')
print(f'O angulo de {angulo} tem COSSENO de {math.cos(math.radians(angulo)):.2f}')
print(f'O angulo de {angulo} tem TANGENTE de {math.tan(math.radians(angulo)):.2f}')

