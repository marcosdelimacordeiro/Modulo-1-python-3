# faca um programa que leia um frase pelo teclado e mostre quantas vezes aparece a letra 'a', em que posicao ela aparece a primeira vez e que posicao ela aparece a ultima vez

frase = str(input('Digite algo pelo teclado: ')).lower().strip()

print(f'Na frase digitada tem total de {frase.count('a')} letras A')
print(f' primeira vez que aparece A e na posicao: {frase.find('a')}')
# pensando como queremos a ultima letra a usa a funcao find, mais como sera a ultima dela usar rfind que ele vai procura a partir da ultima.
print(f'Ultima posicao que aparece A e na posicao: {frase.rfind('a')}')