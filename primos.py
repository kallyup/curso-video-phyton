
def eprimo(num):
    if num < 2:
       return False
    for c in range(2, int(num**0.5)+1):
        if num % c == 0:
            return False
    return True
def primoProximo(num):
    primo = num - 1
    while not eprimo(primo):
        primo -= 1
    return primo
num = int(input('digite um numero: '))
print(primoProximo(num))