# EXERCICIO 14
# C * 1.8 + 32 fahrenheit
# C + 271.15
# EXERCICIO QUE CALCULA A TEMPERATURA AMBIENTE EM °C E TRANSFORMA EM FAHRENHEIT E EM KELVIN
ceusius = float(input('Qual é a temperatura ambiente em °C : '))
fahrenheit = ceusius * 1.8 + 32
kelvin = ceusius + 271.15
print('A temperatura ambiente em Ceusius é : \n {:.2f} \n Em Fahrenheit é : \n {:.2f} \n E em Kelvin é : \n {:.2f} \n'.format(ceusius, fahrenheit, kelvin))