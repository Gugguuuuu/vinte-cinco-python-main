# EXERCICIO 10
# EXERCICIO QUE CONSEGUE CALCULAR QUANTOS REIAS VOCÊ TEM E VERICAR QUANTOS DOLARES VOCÊ QUER E FALAR SE CONSEGUE OU NAO COMPRAR E QUANTO PODE COMPRAR
reais = float(input('Digite quanto dinheiro você tem R$: '))
wantDolars = float(input('Digite quantos dolares você quer comprar U$: '))
dolars = reais / 4.8 
if dolars >= wantDolars:
    print('Você tem {} reais e consegue comprar {} dolares. Mas o total de dolares que você consegue comprar é {:.2f} dolares'.format(reais, wantDolars, dolars))
elif dolars < wantDolars:
    print('Sinto muito mais você so pode comprar {:.2f} dolares'.format(dolars))
