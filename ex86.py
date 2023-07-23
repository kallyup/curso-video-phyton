'''matriz = [[], [], [], [], [], [], [], [], []]
valor = 0
for c in range(0,9):
    valor= int(input(f'digite um valor '))
    matriz[c].append(valor)
print(matriz)
print(matriz[0],[1],[2])
print(matriz[3],[4],[5])
print(matriz[6],[7],[8])
'''
matriz = [[0, 0, 0], [0, 0, 0], [0,0,0]]
for l in range(0,3):
    for c in range(0,3):
            matriz[l][c] = int(input(f'digete um valor para [{l}, {c}]: '))
for l in range(0,3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()