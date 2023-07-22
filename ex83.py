'''expressao = str(input('digite uma expressao '))
abre = 0
fecha = 0
for i in range(0, len(expressao)):
    if expressao[i] == "(":
        abre +=1
    if expressao[i] == ")":
        fecha +=1

if abre == fecha:
    print('expressão valida')
else:
    print('expressão não é valida')'''

expre = str(input('digite sua expressão '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append("(")
    elif simb == ")":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print('xpressão valida')
else:
    print('expressão invalida')