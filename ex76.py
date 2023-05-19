produtos = ('pão', 3.50, 'leite', 7.99, 'queijo', 4.50)
print("-"*40)
print("Mercadinho ASD".center(40))# ou :^40
print("-"*40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')