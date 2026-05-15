# faca um programa que leia tres numeros e mostre qual e o maior e qual e o menor.

n1 = int(input('Digite primeiro numero: '))
n2 = int(input('Digite segundo numero: '))
n3 = int(input('Digite terceiro numero: '))
# verificando o maior
if n1 > n2 and n1 > n3:
    print(f'Maior numero digitado foi {n1}')
elif n2 > n1 and n2 > n3:
    print(f'Maior numero digitado foi {n2}')
elif n3 > n2 and n3 > n1:
    print(f'Maior numero digitado foi {n3}')
# verificando o menor
if n1 < n2 and n1 < n3:
    print(f'Menor numero digitado foi {n1}')
elif n2 < n1 and n2 < n3:
    print(f'Menor numero digitado foi {n2}')
elif n3 < n2 and n3 < n1:
    print(f'Menor numero digitado foi {n3}')