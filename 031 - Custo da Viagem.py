num = float(input('Quantos km vai ser sua viagem: '))
num2 = 0.50 * num
num3 = 0.45 * num
#if num <= 200:
#    print(num2)
#else:
#    print(num3)
print(num2 if num <= 200 else num3)