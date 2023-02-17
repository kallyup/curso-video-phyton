val1 = int(input('digite um valor '))
val2 = int(input('digite outro valor'))

menu = ('''

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números 
[ 5 ] sair

''')
escolha = 0
while escolha <= 5:
    escolha = int(input('escolha'))
    if escolha == 1:
        print(val1 + val2)
    elif escolha == 2:
        print(val1 * val2)
    elif escolha == 3:
        val1 = 0
        if val1 < val2:
            print(val2)
        elif val1 == val2:
            print('valores iguais')
        else:
            print(val1)
    elif escolha == 4:
        val1 = int(input('digite um valor '))
        val2 = int(input('digite outro valor'))
    elif escolha == 5:
        print('fim')
    else:
        print('digite um valor válido')
    print(menu)
