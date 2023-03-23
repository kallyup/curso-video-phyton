import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 5, 10, 15, 20, 25]
plt.plot(x, y)
plt.show()
import numpy as np

z = np.linspace(0, 10, 100)
a = 28 * z
print(a)
from scipy.interpolate import *

b = [0, 3, 6]
c = [0, 2, 0]
p = lagrange(b, c)
print(p)
