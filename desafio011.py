# faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessario para pinta-lo, sabendo que cada litro de tinta pinta uma area de 2m².

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura
total_tinta = area / 2

print(f'A area total da parede e de {area}M², sabendo que cada litros de tinta pode pintar uma area de 2m², voçê vai precisa de {total_tinta} litros de tinta para pintar sua parede.')