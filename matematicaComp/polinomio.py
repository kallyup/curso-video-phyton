'''import numpy as np

# coordenadas dos pontos
x = [0, 2, 4]
y = [0, 4, 16]

# ajuste do polinômio de grau 2 (parábola)
coeficientes = np.polyfit(x, y, 2)

# criação do objeto polinomial
p = np.poly1d(coeficientes)

# impressão do polinômio
print(p)'''
from scipy.interpolate import *
#A(0, 6), B(5, 2) e C(8, 15)
x = [0, 5, 8]
y = [0, 2, 15]
p = lagrange(x, y)
print(p)