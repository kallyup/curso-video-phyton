import random
from time import sleep
n = int(random.uniform(0, 10))
num = 0
c = 0
print('PROCESSANDO....')
sleep(1)
while num != n:
    num = int(input('tente adivinhar '))
    c += 1

    if num == n:
        print('vc acertou')

print(num)
print(f'vc precisou de {c} tentativas')
