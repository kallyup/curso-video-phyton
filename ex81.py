'''lista = []
c = str("Ss")
cont = 0
while c not in 'Nn':
    lista.append(int(input('digite um valor ')))
    cont +=1
    c = input('quer continuar: Ss/Nn')
lista.sort(reverse=True)
if 5 in lista:
        print('achei o 5 na lista')
else:
        print(' 5 não foi encontrado na lista')
print(f' vc digitou {cont} elementos')
print(f'os valores em ordem decrestente são {lista}')
print(lista)'''

valores = []
while True:
    valores.append(int(input('digite um valor')))
    resp = str(input('quer continuar? [S/N]')).upper()
    if resp in 'Nn':
        break
print(f'vc digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem decrescente são {valores}')
if 5 in valores:
        print('achei o 5 na lista')
else:
        print(' 5 não foi encontrado na lista')