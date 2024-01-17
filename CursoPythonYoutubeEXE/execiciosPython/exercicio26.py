# EXERCICIO 26 
# USANDO RANDOM PARA FAZER UM JOGO DE CARA OU COROA
import random
sorteio = random.randint(1, 2)

if sorteio == 1:
    print('Deu cara')
else:
    print('Deu coroa')