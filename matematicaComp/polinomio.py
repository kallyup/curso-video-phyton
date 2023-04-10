import numpy as np

# coordenadas dos pontos
x = [0, 2, 4]
y = [0, 4, 16]

# ajuste do polinômio de grau 2 (parábola)
coeficientes = np.polyfit(x, y, 2)

# criação do objeto polinomial
p = np.poly1d(coeficientes)

# impressão do polinômio
print(p)
