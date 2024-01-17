# EXERCICIO 20
# USANDO random.shuffle PARA EMBARALHAR A LISTA
import random

n1 = str(input('Aluno 1 : '))
n2 = str(input('Aluno 2 : '))
n3 = str(input('Aluno 3 : '))
n4 = str(input('Aluno 4 : '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem de apresentação sera :')
print(alunos)

 