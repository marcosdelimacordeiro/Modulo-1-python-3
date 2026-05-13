# faca um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um numero: '))
# se nao for necessario usar a variavel,mais para frente durante o programa, nao precisa usar variavel, para pode economizar memoria
sucessor = num + 1
antecessor = num - 1

print(f'Voce Digitou o numero {num}, ele tem seu antecessor {antecessor} e o seu sucessor e o numero {sucessor}')
# poderia usar ser as variaveis que fica dessa forma
print(f'valor digitado {num}, o antecessor {num - 1} e o seu sucessor {num + 1}')