maior = 0
menor = 1000000000000000000000

for c in range(5):
    peso = float(input('digite seu peso: '))
    if peso == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso foi {maior}KG  e o menor foi {menor}KG')
