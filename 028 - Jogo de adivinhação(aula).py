from random import randint
from time import sleep
numr = randint(0,5)
print('-=-' *20)
numh = int(input('Qual numero estou pensando entre 0 a 5? '))
print('-=-' *20)
print('PROCESSANDO...')
sleep(2)
if numh == numr:
    print('Acertou, o numero escolhido era {}'.format(numh))
else:
    print('Perdeu, o numero escolhido era {}'.format(numr))
