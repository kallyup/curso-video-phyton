valores = []
for i in range(0, 5):
    n = (int(input(f'digite um valor ')))
    if i == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos,n)
                break
            pos += 1

print(f'os valores em ordem são{valores}')
