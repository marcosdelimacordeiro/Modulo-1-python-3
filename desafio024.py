# crie um programa que leia o nome de uma cidade diga se ela comeca ou nao com o nome 'SANTO'
nome = str(input('Digite o nome da cidade que voce nasceu: ')).strip().upper()

print(nome[:5] == 'SANTO')