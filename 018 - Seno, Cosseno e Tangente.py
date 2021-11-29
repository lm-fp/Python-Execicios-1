from math import sin, cos, tan, radians
an = float(input('digite o angunlo: '))
seno = sin(radians(an))
print('O angulo de {} tem o seno {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O angulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = tan(radians(an))
print('o angulo de {} tem o tangente de {:.2f}'.format(an, tangente))