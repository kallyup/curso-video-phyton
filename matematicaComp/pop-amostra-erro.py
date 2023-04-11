'''A fórmula de Slovin é dada por:

n = N / (1 + N(e^2))

onde:
n = tamanho da amostra
N = tamanho da população
e = margem de erro

Substituindo os valores dados:

N = 150000
e = 0.02

n = 150000 / (1 + 150000(0.02)^2)'''

N = 150000
e = 0.02

n = N / (1 + N * e ** 2)

print(round(n))
