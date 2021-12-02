nome = str(input('Digite uma frase motivadora: ')).strip().lower()
print('A letra a aparece:',nome.count('a'), 'vezes')
print('A letra "A" aparece na primeira posição: {}'.format(nome.find('a')+1))
print('A letra "A" aparece na ultima posição: {}'.format(nome.rfind('a')+1))