# Desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preco da passagem, conbrando R$ 0,50 por Km para viagens de ate 200Km e R$ 0,45 para viagens mais longas

distancia = float(input('Digite distancia total da sua viagem: '))

if distancia <= 200:
    valor = distancia * 0.50
    print(f'Sua viagem tem total de {distancia}Km, o valor total da passagem sera de R$ {valor:.2f} reais.')
else:
    valor = distancia * 0.45
    print(f'Sua viagem tem total de {distancia}Km, o valor da passagem sera total de R$ {valor:.2f} reais.')