nome = str(input('Digite seu nome completo: ')).strip()
print('seu nome maiusculo é: {}'.format(nome.upper()))
print('Seu nome é minuscula é {}'.format(nome.lower()))
print('Seu nome tem {} de letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro tem {} de letras'.format(nome.find(' ')))