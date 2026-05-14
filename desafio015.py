# escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais foram alugado. Calcule o preco a pagar ,sabendo que o carro cursta R$ 60 por dias e R$ 0,15 por km rodado
total_dias = int(input('Digite total de dias que sera alugado: '))
total_km = float(input('Digite total de KM rodados: '))

valor_dias = total_dias * 60
valor_km = total_km * 0.15

total = valor_dias + valor_km   

print(f'O total a pagar e de R$ {total:.2f} reais')