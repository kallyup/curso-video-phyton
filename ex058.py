'''import random
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
print(f'vc precisou de {c} tentativas')'''

from random import randint
comp = randint(0, 10)
print('pensei num numero tente acertar')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual seu palpite'))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador < comp:
            print('mais')
        elif jogador > comp:
            print('menos')
print(f'acertou com{palpites} tentativas')
