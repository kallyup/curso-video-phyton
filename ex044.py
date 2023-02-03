preço = float(input('preço da compra: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] a vista pix ou dinheiro
[ 2 ] cartão a vista
[ 3 ] cartão ate 2x
[ 4 ] cartão 3x ou mais ''')
opção = int(input('digite sua opção'))
if opção == 1:
    print('{}'.format(preço - (preço*0.10)))
elif opção == 2:
    print('{}'.format(preço - (preço*0.05)))
elif opção == 3:
    parcela = preço / 2
    print('o preço é {} a parcela em 2x é {:.2f}'.format(preço, parcela))
elif opção == 4:
    total = preço*1.2
    totparcela = int(input('quantas parcelas? '))
    parcela = total / totparcela
    print('sua compra no valor de {:.2f} foi divida em {}x de {:.2f} com juros'.format(total, totparcela, parcela))
else:
    print('opção invalida')
