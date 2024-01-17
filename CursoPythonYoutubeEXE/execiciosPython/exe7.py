#EXERCICIO 7
# EXERCICIO QUE CALCULA A MEDIA DE NOTAS DE UM ALUNO E DIZ SE ELE PASSOU OU NÂO DE ANO
nota = int(input('Digite sua nota em matematica : '))
nota1 = int(input('Digite sua nota em portugues: '))
nota2 = int(input('Digite sua nota em ciencias : '))
nota3 = int(input('Digite sua nota em geografia : '))
nota4 = int(input('Digite sua nota em historia : '))
media = (nota + nota1 + nota2 + nota3 + nota4) / 5
oquefaltou = 7 - media
if media >= 7:
    print('Você passou!, com {}'.format(media))
else:
    print('Oh você não passou, sua media foi {} e faltou {:.1f} pontos, se esforce mais na proxima '.format(media, oquefaltou))