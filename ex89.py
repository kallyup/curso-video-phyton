'''alunos = []
dados = []
media = 0
med = []
while True:
    dados.append(str(input('digite o nome do aluno ')))
    dados.append(float(input('digite a primeira nota')))
    dados.append(float(input('digite a segunda nota ')))
    alunos.append(dados[:])
    dados.clear()
    cont= input('quer continuar?')
    if cont in 'Nn':
        break
for c in range(0, len(alunos)):
    for n in range(0,3):
       if alunos[c][n] in float:
           media = (alunos[c][n] + alunos[c][n]) / 2

print(media)
print(alunos)'''
ficha = list()
while True:

    nome = str(input('digite o nome do aluno'))
    nota1 = float(input('digite a primeira nota'))
    nota2 = float(input('digite a segunda nota'))
    media = (nota1 + nota2 )/2
    ficha.append([nome, [nota1, nota2], media])
    cont = input('quer continuar?')
    if cont in 'Nn':
        break
print('-='*30)
print(f'numero  Nome : Media :')
print('-='*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*30)
    opc= int(input('mostra nota de qual aluno? (999 para sair)'))
    if opc== 999:
        break
    if opc<=len(ficha)-1:
        print(f' notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('volte sempre')