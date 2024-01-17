# EXERCICIO 6
# EXERCICIO QUE CALCULA O DOBRO TRIPLO E A RAIZ QUADRADA DE UM NUMERO
number = int(input('Digite um numero : '))
d = number * 2
t = number * 3
rq = number ** (1/2)
print('O dobro de {} é \n {} \n o triplo é \n {} \n e a raiz quadrada é \n {:.2f}'.format(number, d, t, rq))
