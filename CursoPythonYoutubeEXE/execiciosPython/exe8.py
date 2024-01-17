# EXERCICIO 8
# E3XERCICIO QUE TRANSFORMA UM VALOR EM METROS PARA CENTRIMETROS E MILIMETROS
metro = float(input('Digite um valor em metros : '))
centimetros = metro * 100
milimetros = metro * 1000
print('{:.2f} metros é igual a : {:.2f} centimetros e igual a {:.2f} milimetros'.format(metro, centimetros, milimetros))