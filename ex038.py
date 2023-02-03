n1 = int(input('digite um valor '))
n2 = int(input('digite outro valor '))
if n1 > n2:
    print('o primeiro valor \033[1;33;40m{}\033[m é maior '.format(n1))
elif n1 < n2:
    print('o segundo valor \033[2;34;40m{}\033[m é maior'.format(n2))
else:
    print('os dois são iguais')
