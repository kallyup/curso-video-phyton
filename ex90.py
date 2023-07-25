'''pessoas = {'nome': 'Gustavo', 'Sexo': 'M', 'idade' : 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = 67 #adiciona ao dicionario
pessoas['nome'] = 'deb' #altera o valor
#del pessoas['Sexo'] deleta
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil =[]
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2= {'uf' : 'São Paulo', 'sigla' : 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])
print(brasil[0]['uf'])'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('digite o nome do estado'))
    estado['sigla']= str(input('digite a silgla do estado'))
    brasil.append(estado.copy()) #para adicionar uma copia não pode usa[:] apenas copy
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')
    print(e)'''

aluno = {}
aluno['nome']= str(input('nome do aluno(a)'))
media = float(input('media do aluno'))
aluno['media'] = media
# ou aluno['media']=float(input('media do aluno'))
if media <= 3: #if aluno['media']<=3
    aluno['situacao'] = 'reprovado'
elif media <=6:
    aluno['situacao'] = 'recuperação'
else:
    aluno['situacao'] = 'aprovado'
print('-='*30)
print(f'Nome: {aluno["nome"]}')
print(f'Media: {aluno["media"]}')
print(f'Situacao: {aluno["situacao"]}')
# ou deb
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')