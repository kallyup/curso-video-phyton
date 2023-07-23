matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]
par = 0
scol= 0
mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor para [{l},{c}]'))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()
print(f'soma dos valores pares {par}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'a soma dos valors da 3 coluna é {scol}')
for c in range(0, 3):
    if matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'o maior numero da coluna 2 é {mai}')
