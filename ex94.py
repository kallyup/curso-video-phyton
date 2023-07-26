dados = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas['nome'] = str(input('digite o nome '))
    pessoas['sexo'] = str(input('digite  sexo: M/F')).upper()
    while True:
        if pessoas['sexo'] not in 'MF':
            print('sexo invalido gite novamente F/M')
            pessoas['sexo'] = str(input('digite  sexo: M/F')).upper()
        else:
            break
    pessoas['idade'] = int(input('digite a idade'))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    cont = input('quer continuar? S/N').upper()
    while True:
        if cont not in 'NS':
            print('opção invalida')
            cont = input('quer continuar? S/N').upper()
        elif cont == 'S':
            break
        else:
            print('ok')
            break
    if cont == "N":
        break
print(f'foram {len(dados)} cadastrados')

media = soma / len(dados)
print(f'a média de idade é de {media:.2f}anos ')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('pessoas a cima da media')
for p in dados:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}:', end='')
        print()
print('<<<ENCERRADO>>>')

