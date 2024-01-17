# EXERCICIO 11
# EXERCICIO QUE CALCULA A AREA DE UMA PAREDE E DIZ QUANTOS LITROS DE TINTA PRESCISA PARA PINTAR
parede = float(input('Digite a altura da sua parade : '))
paredeW = float(input('Digite a largura da sua parede : '))
area = parede * paredeW
tinta= area / 2
print('Uma parede de {:.2f} metros/centimetros e de {:.2f} de largura tem uma area de {:.2f} metros/centimetros quadrados e precisa de {} litros/ML de tinta'.format(parede, paredeW, area, tinta))
