#  EXERCICIO 22
#
nome = str(input('Digite seu nome : '))
nomese = nome.strip()
print('Seu nome com letras maiusculas : ', nome.upper())
print('Seu nome com letras minusculas : ', nome.lower())
print('Quantidades de letras no seu nome ao todo : ', len(nomese) - nomese.count(' '))
nomes = nomese.split()
print('Seu primeiro nome é : {} e tem {} letras '.format(nomes[0], len(nomes[0])))
print('E você tem ', len(nomes) - len(nomes[0]), 'sobrenomes')


