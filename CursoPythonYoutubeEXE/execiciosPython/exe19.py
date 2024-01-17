# EXERCICIO 19
# USANDO BIBLIOTECA RANDOM PARA SORTEA E TAMBEM USANDO random.choice PARA ESCOLHER UM ALUNO ALEATORIO
import random
# alunos = [
#     'Gustavo',
#     'Lucia',
#     'Enzo',
#     'Davi',
#     'Miguel',
#     'Jones',
#     'Robson', 
#     'Geraldo',
#     'Rodolfo',
#     'Cleiton',
#     'Jessica',
#     'Debora', 
#     'Maria',
#     "Heitor",
#     'Rebeca',
#     'Rafael',
#     'Beatriz',
#     'Joaquina',
#     'Guilherme',
#     'Gabriel'
# ]
# srt = random.randint(0, 20)
# alunoEscolhido = alunos[srt]
# print('O aluno escolhido para apagar o quadro foi {}!'.format(alunoEscolhido))
# OU
n1 = str(input('Aluno 1 : '))
n2 = str(input('Aluno 2 : '))
n3 = str(input('Aluno 3 : '))
n4 = str(input('Aluno 4 : '))
alunos = [n1, n2, n3, n4]
alunosSorteado = random.choice(alunos)
print(alunosSorteado)