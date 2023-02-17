acertou = False
while acertou == False:
    s = str(input('digite um sexo biológico válido:'))
    if s == 'm' or s == 'f':
        acertou = True
print(s)