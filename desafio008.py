# escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
metros = float(input('Digite um valor em metros: '))

centimetro = metros * 100
milimetro = metros * 1000

print(f'O valor em metros: {metros} metros\nO valor em centimetros: {centimetro} centimetros(cm)\nOvalor em milimetros: {milimetro} milimetros(mm)')