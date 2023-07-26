'''jogador = {}
jogador['nome'] = str(input('nome do jogador? '))
partidas = int(input('quantas partidas ele jogou? '))
gols = list()
total = 0
for i in range(0, partidas):
    gol = (int(input(f'quantos gols marcou na partida {i+1}? ')))
    total += gol
    gols.append(gol)
    jogador['gols'] = gols.copy()
    jogador['total'] = total
print('-='*30)
print(jogador)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print()
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {partidas} partidas')
'''

jogador = dict()
partidas = list()
jogador['nome']= str(input('nome do jogador'))
tot = int(input(f'quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append((int(input(f'quantos gols ele fe na partida {c+1}'))))
jogador['gols']= partidas[:]
jogador['total']= sum(partidas)
print('-='*30)
print(jogador)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {tot} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' => na partida {i+1} fez {v} gols')
print(f'foi um total de {jogador["total"]} gols')
