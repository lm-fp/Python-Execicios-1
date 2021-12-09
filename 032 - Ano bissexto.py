ano = int(input('Digite o ano: '))
num = ano%4
print('Ano Bissexto' if num == 0 else 'O ano nao é bissexto')