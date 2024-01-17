# EXERCICIO 12
# EXERCICIO QUE CALCULA DESCONTO SE O USUARIO COLOCAR O CUMPO CERTO
pedido = str(input('Digite o seu pedido? '))
qualValor = float(input('Qual é o preço do pedido? '))
cupom = str(input("Digite o cupom : "))
valorFinal = qualValor - (qualValor * 5 / 100)
if cupom == "happyNewYear":
    print('O/A {} fica com 5% de desconto por causa do cumpom. Saindo de {:.2f} reais para {:.2f} reais'.format(pedido, qualValor, valorFinal))
else:
    print('Cupom errado fica {} reais. Qual forma de pagamento?'.format(qualValor))