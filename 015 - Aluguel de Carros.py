dias = int(input('Quantos dias vc ficou com o carro: '))
km = float(input('Quantos km vc andou: '))
pagar = (60 * dias ) + (0.15 * km)
print(' Voce tera que pagar {:.2f}'.format(pagar))