num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
num3 = int(input('Digite o ultimo valor: '))

menor = num1
maior = num1

if num2<menor and num2<num3:
    menor = num2
if num3<menor and num3<num2:
    menor = num3
print('menor: ',menor)

if num2>maior and num2>num3:
    maior = num2
if num3>maior and num3>num2:
    maior=num3
print('o maior é ',maior)
