km = float(input('quantos km rodou?'))
dias = int(input('quabtis dias? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f}'. format(pago))
