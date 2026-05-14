# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porcao inteira
from math import trunc
# foi importado metodo especifico

n = float(input('Digite um valor: '))
ni = trunc(n)
print(f'O valor digitado foi {n} e a sua porcao inteira é {ni}')
