from math import hypot
co = float(input('qual o cateto oposto: '))
ca = float(input('qual o cateto adjacente: '))
qa = hypot(co, ca)
print('A hipotenusa é {:.2}'.format(qa))