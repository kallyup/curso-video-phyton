''''#questão 2
p = True
q = True
r = False
a = p or q
print(a)
b = p or r
print(b)
c = p or q and r
print(c)
d = not(p or q and r)
print(d)
e = q and r
print(e)
f = not p
print(f)
g = not(p and r)
print(g)
#questão 3
usuario = int(input('digite a senha '))
senha = 705080
if usuario == senha:
    print('acesso liberado')
else:
    print('acesso negado')
#questão 4

renda = float(input('digite seu salário '))
financiamentos = float(input('digite o valor de algum outro finciamnto se tiver '))
tot = (renda / 100)*20
if renda < 8500:
    print('financimaneto negado')
elif financiamentos >= tot:
    print('financiamento negado')
else:
    print('financiamento aprovado') '''

# questão 5

atvp1 = float(input('digite a nota da primeira atv prática '))
atvp2 = float(input('digite a nota da segunda atv prática '))
prova = float(input('digite a nota da prova objetiva '))
passou = (atvp1*0.2) + (atvp2*0.3) + (prova*0.5)
if passou > 30:
    print('reprovado')
elif passou >= 70:
    print('passou')
else:
    print('recuperação')

# questão 6

senha = int(input('digite a senha '))
if senha == 705080 or senha == 999999:
    print('acesso permitido')
else:
    print('acesso negado')

# questão 7

p = False
q = True

