import random
import numpy as np

numero = np.random.randint(1, 9999, (5))
print(numero)
numero.sort()
print(numero)
print("menor valor ", (numero[0]))
print('maior valor ', (numero[-1]))

