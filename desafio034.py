# Escreva um programa que pergunte o salario de um funcionario e calcula o valor do seu aumento. Para salario superiores a R$ 1250,00, calcule um aumento de 10%. para os inferiores ou iguais, o aumento e de 15%.

salario = float(input('Qual e o seu salario : '))

if salario > 1250:
    novo_salario = salario + (salario * (10/100))
    print(f'O seu novo salario e de R$ {novo_salario:.2f} reais')
else:
    novo_salario = salario + (salario * (15/100))
    print(f'O seu novo salario e de R$ {novo_salario:.2f} reais')
