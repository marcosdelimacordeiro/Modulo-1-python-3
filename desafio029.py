# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar  80km/h, mostre a mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite

velocidade = int(input('Digite a sua velocidade '))
total_vel = 0 
if velocidade > 80:
    total_vel = velocidade - 80
    valor = total_vel * 7 
    print(f'Voce sera Multado! Voce estava {total_vel}Km/h acima do permitido, que tem uma multa de R$ 7,00, por km/h acima de 80km/h, o valor da sua multa e de R$ {valor:.2f}')
else:
    print(f'Parabens! Voce esta dentro da velocidade permitida, continue assim sendo bom condutor!')