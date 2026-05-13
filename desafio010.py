# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. considere US$1,00 = R$ 3,27

valor = float(input('Quantos reias voce tem na carteira: '))

conversao = valor / 3.27

print(f'Voce tem na carteira o valor R$ {valor:.2f} reais , convertidos para dolares voce tem o valor de US$ {conversao:.2f} dolares.')