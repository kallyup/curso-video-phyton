'''from calendar import isleap
ano = int(input('digite o ano '))
if isleap(ano):
    print('é bissexto')
else:
    print('não é bissexto')'''

from datetime import date
ano = int(input('que ano quer saber? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ano é bissexto')
else:
    print('ano não é bissexto')