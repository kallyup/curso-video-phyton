'''import numpy as np

notas = [8, 7, 9, 10, 2, 7, 9, 10, 9, 3, 8, 5]

desvio_padrao = np.std(notas)

print(f"O desvio padrão é de {desvio_padrao:.2f}")'''

import numpy as np

valores = np.array([67.8, 78.6, 54.4, 98.6, 99.4, 130.8, 142.6, 161.6, 142.5, 158.4])
desviop = np.std(valores)
print(f"O desvio padrão é de {desviop:.2f}")

'''import scipy.stats
media= 90000
desvio_padrao= 4000
X = 95000
a = scipy.stats.norm(media, desvio_padrao).cdf(X)-0.5
print(a)

from scipy.stats import norm

p = norm.cdf(1.25) - norm.cdf(0)
print(p)'''

