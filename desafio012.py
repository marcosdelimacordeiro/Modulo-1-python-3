# faca um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o valor do produto: '))

novo_preco = preco - (preco * (5/100))

print(f'Valor do produto: {preco:.2f} reais\nCom desconto de 5% no valor ele fica  R$ {novo_preco:.2f} reais')