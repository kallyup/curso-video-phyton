from scipy.stats import norm

media = 12000
desvio_padrao = 800
x1 = 10000
x2 = 12000

z1 = (x1 - media) / desvio_padrao
z2 = (x2 - media) / desvio_padrao

probabilidade = norm.cdf(z2) - norm.cdf(z1)

print(f"A probabilidade é de {probabilidade*100:.2f}%")
