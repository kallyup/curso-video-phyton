'''
retira espaços
frase = str(input('digite uma frase: '))
frase = ''.join(frase.split())
ou
frase = str(input('digite uma frase: '))
frase = frase.replace(' ', '')'''

frase = str(input('digite uma frase: ')).strip().lower()
frase = frase.replace(' ', '')
if frase == frase[::-1]:
    print('é polindromo')
else:
    print('não é')
print(frase)

'''frase = str(input('digite uma frase')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
invero = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo')
else:
    print('naõ é palindromo)
'''