resp = 'S'
soma = quant = media = 0
while resp in 'Ss':
    num = int(input('digite um numero'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    resp = str(input('quer contiar [S/N]'))
media = soma / quant
print(f'vc digitou {quant} numeros e amedia foi {media} ')
print(f'o maior foi {maior} e o menor foi {menor}')