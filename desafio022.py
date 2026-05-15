# crie um programa que leia o nome completo de uma pessoa mostre
# o nome com todas as letras maiuscula e minusculas
#Quantas letras ao todo(sem considera espacos)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: '))

print(f'O nome com letra maiusculas fica {nome.upper()}\nJa o nome com letras minusculas fica {nome.lower()}')
print(f'Seu nome tem todas de {len(nome.strip())} letras.')

nomes = nome.split()
print(f'Seu primeiro nome tem {len(nomes[0])}')

