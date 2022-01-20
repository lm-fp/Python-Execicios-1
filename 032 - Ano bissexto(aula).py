from datetime import date
ano = int(input('Digite o ano: ou coloque 0 para o ano atual: '))
if ano ==0:
    ano = date.today().year
num = ano%4
print('Ano Bissexto' if ano%4 ==0 and ano%100 != 0 or ano %400 ==0  else 'O ano nao é bissexto')