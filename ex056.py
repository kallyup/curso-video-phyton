somaIdade = 0
media = 0
maioridadeHomem = 0
nomeVelho = ''
totF20 = 0
for p in range(5):
    print(f'--------{p}° pessoa ---------')
    nome = str(input('digite seu nome:')).strip()
    idade = int(input('digite sua idade: '))
    sexo = str(input(' sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maioridadeHomem:
        maioridadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade <20:
        totF20 += 1
media = somaIdade / 4
print(f'á media da idade do grupo é: {media} anos')
print(f'o homem mais velho tem {maioridadeHomem} anos e se chama {nomeVelho}')
print(f'ao todo {totF20} mulheres com menos de 20 anos')
