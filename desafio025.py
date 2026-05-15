# crie um programa que leia o nome de uma pessoa e diga se ela tem 'SIlVA' no nome

nome = str(input('Digite o seu nome: ')).strip().lower()

print(f'Seu nome tem Silva: {'silva' in nome}')