# Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 e peca para o usuario tentar descobrir qual foi o numero escolhido pelo computador. o programa devera escrever na tela se o usuario venceu ou perdeu

from random import randint
n = randint(0,5)
print('=-'*30)
print('Vou tentar Pensar em numero entre 0  e 5, agora sua vez tente adivinhar...')
print('=-'*30)
num = int(input('Digite um numero entre 0 e 5: '))
print('=-'*30)

if n == num:
    print(f'Parabens voce acertou! Pensamos no mesmo numero {n}')
else:
    print(f'Nao foi dessa vez, voce errou! Pensei no numero {n}, e voce no numero {num}')