import numpy as np

notas = [8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]

desvio_padrao = np.std(notas)

print(f"O desvio padrão é de {desvio_padrao:.2f}")
