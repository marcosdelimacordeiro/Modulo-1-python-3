# faca um programa que leia um numero de 0 9999 e mostre na tela cada um dos digitos separados
numero = int(input('Informe um numero: '))

milhar = numero // 1000 % 10
centena = numero // 100 % 10 
dezena = numero // 10 % 10
unidade = numero // 1 % 10

print(f'''
Analisando o numero {numero}
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
''')