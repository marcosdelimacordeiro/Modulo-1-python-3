# um professor que sortear um dos seus quatros alunos para apagar o quadro, faca um programa que ajude ele, lendo nome dos alunos e escrevendo na tela o nome do escolhido
from random import choice

nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
# usa funcao choice que e uma escolha dentro da lista
lista = [nome1,nome2,nome3,nome4]
sort = choice(lista)
print(f'O aluno escolhido foi {sort}')