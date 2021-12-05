n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
m = (n1+n2)/2
print('Sua media foi {}'.format(m))
print('Reprovado' if m<=6 else 'Aprovado')