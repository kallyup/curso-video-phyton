from  random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura',)
computador = randint(0, 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('ESCOLHA UMA OPÇÃO '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-=' * 15)
print('computado escolheu {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('jogador VENCEU')
    elif jogador == 2:
        print('computador VENCEU')
    else:
        print('jogada inválida')
elif computador == 1: #papel
    if jogador == 0:
        print('computador VENCEU')
    elif jogador == 1:
        print('IMPATE')
    elif jogador == 2:
        print('jogador VENCEU')
    else:
        print('jogada inválida')
elif computador == 2: #tesoura
    if jogador == 0:
        print('jogador VENCEU')
    elif jogador == 1:
        print('computador VENCEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('jogada inválida')


