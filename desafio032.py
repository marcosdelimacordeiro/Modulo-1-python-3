# faca um programa que leia qualque ano e mostre se ele e bissexto
ano = int(input('Digite o ano: '))
# ano bissexto e divisivel por 4 ,resto 0, depois divisao por 100 nao pode ser 0 , e tambem ele tem que ser divisel por 400 divisao exata
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano digitado e um ANO BISSEXTO!')
else:
    print(f'O ano digitado NAO E BISSEXTO!')