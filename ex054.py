from datetime import date

atual = date.today().year
maior = 0
menor = 0
for c in range(7):
    nacimento = int(input('que ano vc nasceu?'))
    idade = atual - nacimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} atigiram a maior idade e {menor} não')

'''maior = 0
menor= 0
for c in range(7):
    idade = int(input('digite a idade: '))
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} atigiram a maior idade e {menor} não')'''
