def escreva(text):
    tam = len(text) + 4
    print("~" * tam)
    print(f'{text}')
    print("~" * len(text))

escreva((str(input('digite a frase'))))