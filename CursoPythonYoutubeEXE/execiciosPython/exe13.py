# EXERCICIO 13
# EXERCICIO QUE CALCULA QUANTOS NEGOCIOS FECHOU E DEPENDENDO DISSO ELE GANHARA UM AUMENTO OU NÃO
funcionario = str(input('Digite o nome do funcionario : '))
salario = float(input('Digite qual é o salario do funcionario : '))
negocios = int(input('Digite quantos negocios esse funcionario fechou : '))
if negocios >= 50:
    salarioA = salario * 0.15
    aumento = salario + salarioA
    print('O funcionario {} recebera um aumento de 15% pois, conseguiu fechar {} negocios(medios/grandes) saindo de um salario de {:.2f} para {:.2f} reais'.format(funcionario, negocios, salario, aumento))