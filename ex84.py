'''test = []
test.append('deb')
test.append(25)
galera = list()
galera.append(test[:])
test[0]= 'maria'
test[1]= 22
galera.append(test[:])
print(galera)'''

'''galera = [['joão', 25],['lucas', 32], ['deb',27], ['rafa',12]]
print(galera[3][1])'''

'''galera = [['joão', 25],['lucas', 32], ['deb',27], ['rafa',12]]
for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} idades')'''

'''galera = list()
dado = list()
totmai = totmen =0
for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1]>= 21:
        print(f'{p[0]} é maior de idade')
        totmai +=1
    else:
        totmen+= 1
        print(f'{p[0]} não é maior de idade')
print(f"{totmen} menores e {totmai}maiores")'''

pessoas = []
dados = []
pesadas = 0
leves = 0
while True:
    dados.append(str(input('digite seu nome ')))
    dados.append(float(input('digite seu peso ')))
    if len(pessoas)== 0:
        pesadas = leves = dados[1]
    else:
        if dados[1]> pesadas:
            pesadas = dados[1]
        if dados[1]< leves:
            leves = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont = input('quer continuar')
    if cont in "Nn":
        break
print(f'fora cadastradas {len(pessoas)} pessoas')
print(f'as mais pesadas tinham {pesadas}kg . peso de', end='')
for p in pessoas:
    if p[1] == pesadas:
        print(f' [{p[0]}]', end='')
print()
print(f'as mais leves tinha {leves}kg e foram', end='')
for p in pessoas:
    if p[1] == leves:
        print(f'[{p[0]}]', end='')
print()

