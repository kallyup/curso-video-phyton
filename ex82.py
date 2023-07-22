valore = list()
impar = list()
par = list()
while True:
    valore.append(int(input("digite um valor")))
    continuar = input('quer continuar digitando? Ss/Nn')
    if continuar in "Nn":
        break
for i, valor in enumerate(valore):
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
print(f'Lista Completa {valore}')
print(f'Pares {par}')
print(f'Impares {impar}')

'''num = list()
par = list()
impar = list()

while True:
    num.append(int(input('Digite um numero')))
    resp = str(input('quer continuar? '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'lista completa{num}')
print(f'Pares {par}')
print(f'impares {impar}')'''

