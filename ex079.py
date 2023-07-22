numeros = []
while True:
    n = int(input('digite um valor'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('valor duplicado')
    r = str(input('quer continuar'))
    if r in 'Nn':
        break
print(numeros)



'''
valores =[]

while True:
    valor = (input("Digite um valor (ou 'sair' para encerrar): "))
    if valor.lower() == 'sair':
        break
    elif valor.isdigit():
        valor = int(valor)
        if valor not in valores:
            valores.append(valor)
            print('valos adicionado a lista')
        else:
            print('valor já existente ')
    else:
        print('entrada invalida')
    valores.sort()
print('valores em ordem crescente')
for valor in valores:
    print(valor)

print(valores)


def adicionar_valores_unicos():
    valores = []
    while True:
        valor = input("Digite um valor (ou 'sair' para encerrar): ")
        if valor.lower() == "sair":
            break
        elif valor.isdigit():
            valor = int(valor)
            if valor not in valores:
                valores.append(valor)
                print("Valor adicionado à lista!")
            else:
                print("O valor já existe na lista. Ignorando...")
        else:
            print("Entrada inválida. Digite apenas números inteiros.")

    valores.sort()
    print("Valores em ordem crescente:")
    for valor in valores:
        print(valor)


adicionar_valores_unicos()'''