salario_atual = float(input('Digite seu salario: '))

a15 = (salario_atual * 0.15) + salario_atual
a10 = (salario_atual * 0.10) + salario_atual

if salario_atual > 1250:
    print('aumento 10: {:.2f}'.format(a10))
else:
    print('aumento 15: {:.2f}'.format(a15))
