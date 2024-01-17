# EXERCICIO 17
# EXERCICIO QUE CALCULA A HIPOTENUZA DE UM TRIANGULO RETANGULO
import math
c1 = float(input('Digite o valor do primeiro cateto : '))
c2 = float(input('Digite o valor do segundo cateto : '))
i = math.hypot(c1, c2)
# i = math.sqrt((c1 ** 2) + (c2 ** 2))
print('Um triangulo retangulo com o primero cateto sendo : \n {:.2f} \n E o segundo sendo : \n {:.2f} \n A hipotenuza sera : \n {:.2f} \n'.format(c1, c2, i))
