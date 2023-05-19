numero = (int(input('digite um núemro ')),
          int(input('digite mais um núemro ')),
          int(input('digite outro núemro ')),
          int(input('digite um núemro ')))

print(f' vc digitou os valores {numero}')
print(f' o valor nove apareceu {numero.count(9)} vezes')
if 3 in numero:
    print(f'o valor 3 aparecereu na {numero.index(3)+1} posição')
else:
    print('o valor 3 não foi digitado')
print('os valores pares digitados foram ', end=" ")
for n in numero:
    if n % 2 == 0:
        print(n, end=" ")
