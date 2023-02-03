#estruturas condicionais if elif else

salario = float(input('qual seu salário? '))
valor = float(input('qual o valor da casa? '))
anos = int(input('em quantos anor quer pagar? '))
meses = anos * 12
prestacao = valor / meses
if prestacao >= salario * 0.3:
    print('não pode comprar a casa seu liso')
else:
    print('pode comprar a casa com prestaçoes de {:.2f} mensais'.format(prestacao))