velocidade = float(input('Qual sua velocidade: '))
multa = (velocidade-80) * 7
print('Multa de R${:.2f}'.format(multa) if velocidade >=80  else 'Otimo, esta respeitando as leis')