# EXERCICIO 3
# EXERCICIO QUE VERICA TODOS VALORES DE UMA ENTRADA
value = input('Digite alguma coisa : ')
print('So tem letras?', value.isalpha())
print('So tem numeros?', value.isnumeric())
print('So tem letras maiusculas?', value.isupper())
print('So tem letras minusculas?', value.islower())
print('So tem espaços?', value.isspace())
print('So tem codigo em ASCII?', value.isascii())
print('É um titulo?', value.istitle())
print('So tem decimal?', value.isdecimal())
print('So tem digito?', value.isdigit())         
print('É printavél?', value.isprintable())
print('É identificavel', value.isidentifier())
isnumber = ('Digite algo')
if isnumber.isnumeric() == True:
    print("você acertou")