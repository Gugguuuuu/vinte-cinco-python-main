n = str(input('Digite seu nome completo : '.strip()))
c = n
n = n.split()
print('Olá {}!, prazer em te conhecer \n Seu primeiro nome é : {} \n Seu utimo nome é : {}'.format(c, n[0], n[-1]))