jogador = dict()
partidas = list()
time = list()
# ler dados e adiconar na lista e no dicionario
while True:
    jogador.clear()
    jogador['nome'] = str(input('digite o nome do jogador'))
    tot = int(input(f'quantas partidas o jogador {jogador["nome"]} jogou?'))
    partidas.clear()
    for i in range(0, tot):
        partidas.append(int(input(f'quantos gol o jogador {jogador["nome"]} marcou na partida {i+1}')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
# pergunta se quer adicionar mais
    while True:
        cont = str(input('quer continuar S ou N')).upper()[0]
        if cont in "SN":
            break
        print('digite um valor valido S ou N')
    if cont == "N":
        break
#cabeçalho
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-'*40)
#resultados
for k, v in enumerate(time):
    print(f' {k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(('-'*40))
while True:
    busca = int(input('mostrar dados de qual jogador? 999 para'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'não exites esse jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'  no jogo {i+1} fez {g} gols')
    print(('-'*40))
print('<<VOLTE SEMPRE>>')
