from random import randint
numr = randint(0,5)
numh = int(input('Qual numero estou pensando entre 0 a 5? '))
print('Acertou, o numero escolhido era {}'.format(numh) if numh ==numr else 'Perdeu, o numero escolhido era {}'.format(numr))
'''if numh == numr:
    print('Ganhou')
else:
    print('Perdeu')'''
