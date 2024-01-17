# EXERCICIO 9
# EXERCICIO QUE CALCULA A TABUADA DE  QUALQUER NUMERO
num = int(input('Digite um numero : '))
for i in range(10):
    i = i + 1
    print('{} x {} = {}'.format(num, i, num * i))