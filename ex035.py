r1 = float(input('valor da primeira reta'))
r2 = float(input('valor da segunda reta '))
r3 = float(input('valor da terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' as retas formam um triangulo')
else:
    print('essas restas não forma triangulo')