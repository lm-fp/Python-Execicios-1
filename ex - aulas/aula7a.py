n1 = int(input('um valor: '))
n2 = int(input('segundo valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('a soma vale {} e a multipilicação é {} e a divisao é {:.2f}'.format(s, m, d), end='')
print('a divisao inteira é {}, e a exponeciacao é {}'.format(di, e))
