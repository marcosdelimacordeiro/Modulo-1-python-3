# o mesmo professor do desafio 19 quer sortear a ordem de apresentacao de trabalhos dos aluno. faca um programa que leia o nome dos quatros aluno e mostre a ordem sorteado
import random

n1 = str(input('digite um nome: '))
n2 = str(input('digite um nome: '))
n3 = str(input('digite um nome: '))
n4 = str(input('digite um nome: '))

lista = [n1,n2,n3,n4]
# usa a funcao shuffle, que quer dizer embaralhar 
random.shuffle(lista)

print(f'A ordem de apresentacao será: \n{lista}')