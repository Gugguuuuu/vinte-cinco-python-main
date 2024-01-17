# EXERCICIO 28
# MANIPULANDO STRINGS E FAZENDO E CODIGO DE DESCRIPTOGRAFAR UM CODIGO
from time import sleep

frase = ' GywUweSerTwsAfzVtyOp Éd MveUefIggTfgOk BhjOjkNloIptTdzÃeqO '

print('Você tera que digitar tres numeros para descriptgrafar o codigo')

sleep(3)

print('Esse é o codigo: \n {}'.format(frase))
print('O comprimento do codigo é :', len(frase))

sleep(3)

n1 = int(input('Digite o primeiro numero : '))
n2 = int(input('Digite o segundo numero : '))
n3 = int(input('Digite o terceiro numero : '))

if n1 == 1 and n2 == 60 and n3 == 3:
    print('Parabens, você acertou o codigo descriptografado era : ', '-'.join(frase[n1:n2:n3]))
else:
    print('Você errou preste mais atenção')