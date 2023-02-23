'''n = c = soma = 0
while n != 999:
    n = int(input('digite um numero '))
    if n <= 998:
        c += 1
        soma += n
    else:
        print(c)
print('fim')
print(soma)'''

num = cont = soma = 0
num = int(input('digite um numero'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('digite um número:'))
print(f'vc digitou {cont} numeros e a soma foi {soma}')
