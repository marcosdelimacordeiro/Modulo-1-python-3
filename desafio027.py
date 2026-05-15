# Faca um programa que leia nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input('Digite o seu nome completo: '))
nomes = nome.split()
print('Muito Prazer em te conhecer!')
print(f'Seu primeiro nome é {nomes[0]}')
print(f'Seu ultimo nome e {nomes[-1]}')