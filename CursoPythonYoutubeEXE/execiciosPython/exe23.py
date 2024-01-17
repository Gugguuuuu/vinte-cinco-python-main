# Exercicio 23
num = int(input('Digite um numero de 1 á 9999 : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 1000
print('Unidades : ', u)
print('Dezenas : ', d)
print('Cemtenas : ', c)
print('Unidades de milhar : ', m)
