from datetime import date
ano = int(input('digite eu ano de nascimento '))
atual = date.today().year
idade = atual - ano
if idade <=9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <=19:
    print('junior')
elif idade <= 25:
    print('senior')
else:
    print('master')
