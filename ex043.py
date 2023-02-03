peso = float(input('digite seu peso em kg '))
altura = float(input('digite sua altura em metros '))
imc = peso / (altura**2)
if imc <= 18.5:
    print('abaixo do peso')
elif imc <= 25:
    print('peso ideal')
elif imc <= 30:
    print('sobrepeso')
elif imc <= 40:
    print('obesidade')
else:
    print('obesidade morbida')
