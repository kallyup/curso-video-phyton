nome = preço = total = produto = 0
barato = 999999
nbarato = 0
continuar = 'S'.strip().upper()
while continuar != 'N':
    nome = str(input('o que vc comprou '))
    preço = float(input('quanto custou '))
    total += preço
    if preço > 1000:
        produto += 1
    if preço < barato:
        barato = preço
        nbarato = nome
    continuar = (input('quer continuar [S/N]')).strip().upper()
print(f'o total da compra foi :{total} tiveram {produto} que custavam mais de R$1000 e o produto mai barato foi : {nbarato}')
