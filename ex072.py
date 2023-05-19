'''lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(len(lanche))

for cont in tange(0, len(lanche)):
    print(f'eu vou comer {lache[cont]}')
    
for comida in lanche:
    print(f'eu vou comer {comida}')
    
print('comi pra caramba')
for pos, comida in enumerate(lanche):
    print(f'eu vou comer {comida} na posição {pos}')

'''


numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
usuario = int(input('digite um número entre 0 e 10 : '))
'''parar = False
while parar == False:
    if 10 >= usuario >= 0:
        print(numeros[usuario])
        parar = True
    else:
        usuario = int(input('digite um número entre 0 e 10 : '))'''
while True:
    usuario = int(input('digite um número entre 0 e 10 : '))
    if 0 <= usuario <= 10:
        break
    print("tente novament", end="")
print(f"vc digitou o numero {numeros[usuario]}")
