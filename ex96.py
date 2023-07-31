'''def contador(* num):
    tam = len(num)
    print(f'recebi os valores {num} e são ao todo {tam} numeros')
    soma = sum(num)
    print(soma)

contador(2, 3, 4, 1)
contador(1, 4, 5, 7, 8, 9, 10)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1


val = [5,4,5,3,2,1,3,5]
dobra(val)
print(val)
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"a soma dos valores {valores} temos {s}")


soma(2,4)
soma(5,4,6)'''

def area(l,c):
    print('AREAS DO TERRENO')
    print('-='*20)
    soma = l * c
    print(f'a area de um terreno {l} x {c} é de {soma}')


area((float(input(' digite a largura'))), (float(input(' digite o comprimento'))))

def area2(larg, comp):
    a = larg* comp
    print(f'a area de um terreno {larg} x {comp} é de {a}')


print(' controle de terrenos ')
print('-'*20)
l = float(input('digite a largura'))
c = float(input('digite o comprimento'))
area2(l,c)