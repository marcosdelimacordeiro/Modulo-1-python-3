# faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com aumento de 15%.

salario = float(input('Digite seu salario: '))

novo_salario = salario + (salario*(15/100))

print(f'Seu salario atual e no valor de R$ {salario:.2f} reais\nCom reajuste de 15% no salario\nO novo valor do seu salario sera R$ {novo_salario:.2f} reais.')