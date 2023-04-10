'''import numpy as np

notas = [8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]

desvio_padrao = np.std(notas)

print(f"O desvio padrão é de {desvio_padrao:.2f}")'''

import numpy as np

valores = np.array([67.8, 78.6, 54.4, 98.6, 99.4, 130.8, 142.6, 161.6, 142.5, 158.4])
desviop = np.std(valores)
print(f"O desvio padrão é de {desviop:.2f}")
