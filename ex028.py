'''tempo = int(input('quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
print('---FIM---')

ESSE OU ESSE FORMAS DE FAZER

tempo = int(input('quantos anos tem seu carro? '))
if tempo <=3:
    print("carro novo")
else:
    print('carro velho')
print('---FIM---')

n1 = float(input('digite uma nota: '))
n2 = float(input('digite outra nota: '))
m = (n1 + n2) / 2
print('sua nota foi {: 1f}'.format(m))
if m <= 6.0:
    print('vc é burro')
else:
    print('vc passou')

print('vc é burro' if m <= 6.0 else 'vc passou')'''

import random
from time import sleep
n = int(random.uniform(0, 5))
num = int(input('tente adivinhar '))
print('PROCESSANDO....')
sleep(3)
if num == n:
    print('vc acertou')
else:
    print('{} vc errou'.format(n))

'''
from random import randint
computador = randint(0, 5) faz o computadr sortear
print('pensei no numero{}'.format(computador))
'''

