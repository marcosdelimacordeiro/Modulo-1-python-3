# Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou Impar

numero =int(input('Digite um numero inteiro: '))
if numero % 2 == 0:
    print(f'O numero que voce digitou {numero}, ele e um numero PAR!')
else:
    print(f'O numero {numero} que voce digitou e numero IMPAR!')