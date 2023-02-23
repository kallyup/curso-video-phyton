acertou = False
while acertou == False:
    s = str(input('digite um sexo biológico válido:'))
    if s == 'm' or s == 'f':
        acertou = True
print(s)

'''sexo = str(input('informe seu sexo:')).split().upper()[0]
while sexo not in 'MmFm':
    sexo = str(input('dados invalidos'))
print(sexo)'''