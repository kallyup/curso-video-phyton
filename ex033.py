n1 = int(input('digite um número '))
n2 = int(input('digite outro número '))
n3 = int(input('digite outro numero '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3< n2:
    menor=n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    menor = n3
print('o menor é \033[3;35;42m{}\033[m'.format(menor))
print('o maior é \033[2;32;47m{}\033[m'.format(maior))


