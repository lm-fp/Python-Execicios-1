r1 = float(input('Digite um valor: '))
r2 = float(input('Digite outro valor: '))
r3 = float(input('Digite o ultimo valor: '))

if r2 < r1+r3 and r3 < r1+r2 and r1 < r2+r3:
    print('pode formar um triangulo')
else: print('nao pode')
