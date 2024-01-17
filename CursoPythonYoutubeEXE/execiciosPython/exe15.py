# EXERCICIO 15
# EXERCICIO QUE CALCULA O ALUGUEL A SE PAGAR POR UM CARRO POR KM RODADO E DIAS ALUGADOS
diasAlugados = int(input('Digite quantos dias você alugou o carro : '))
kmRodados = float(input('Digite quantos KM você rodou : '))
aluguel = (diasAlugados * 60) + (kmRodados * 0.15)
print('Com {} dias de aluguel e {:.2f} km rodados, seu aluguel sera de {:.2f}R$.'.format(diasAlugados, kmRodados, aluguel))