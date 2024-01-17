# EXERCICO 18
# CODIGO QUE CALCULA O SENO COSSENO E TANGENTE A PARTIR DE UM NUMERO
import math
a = float(input('Digite um angulo qualquer ° : '))
an = math.radians(a)
s = math.sin(an)
c = math.cos(an)
t = math.tan(an)
print('Com o angulos {:.2f} o seno sera : \n {:.2f} \n O cosseno sera : \n {:.2f} \n E a tangente sera : \n {:.2f} \n'.format(an, s, c, t))   