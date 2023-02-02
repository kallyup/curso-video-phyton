v = float(input('digite a velocidade: '))
if v >= 80:
    print('vc foi multado')
    m = (v-80)*7
    print('a multa é de R${:.2f}'.format(m))
print('tenha um bom dia')
