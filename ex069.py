continuar = 'S'.strip().upper()
maior = 0
menor = 0
hom = 0
while continuar != 'N':
    sexo = str(input('digite seu sexo: M/F ')).strip().upper()
    idade = int(input("digite sua idade: "))

    if sexo == 'M':
        hom += 1
    if idade > 18:
        maior += 1
    if sexo == 'F' and idade < 20:
        menor += 1
    continuar = str(input('quer continuar? [S/N] ')).strip().upper()
print(f'exixtem {maior} maior de 18 anos {hom} homens e {menor} mulheres tem menos de 20 anos')
