'''from math import pow
#import math
co = float(input('qual o valor do cateto oposto? '))
ca = float(input('qual o valor do cateto adjacente? '))
#h = math.pow(ca, 2) + math.pow(co, 2)
h = (pow(ca, 2) + pow(co, 2)) ** (1/2)
print(' hipotenusa {} é a soma do quadrado dos catetos oposto {} e adjacente {}'.format(h, co, ca))'''

import math
co = float(input('qual o valor do cateto oposto? '))
ca = float(input('qual o valor do cateto adjacente? '))
hi = math.hypot(co,ca)
print(hi)

