valor = []
for c in range(0, 5):
    valor.append(int(input(f'digite um valor para posição {c}: ')))
    if c == 0:
        maior = menor = valor[c]
    else:
        if valor[c] > maior:
            maior = valor[c]
        if valor[c] < menor:
            menor = valor[c]
print('='*30)
print(f'vc digitou {valor}')
print(f'o maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valor):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'o menor valor foi {menor} nas posiçoes', end='')
for i, v in enumerate(valor):
    if v == menor:
        print(f'{i}... ', end='')
'''print(valor)'''
print()