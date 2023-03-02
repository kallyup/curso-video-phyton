print("----Programa de taboada----")
print('#para sair digite um número negativo')
n = 1
c = 0
while n > 0:
    n = int(input('digite um numero para saber a taboada'))
    c = 0
    while c != 10 and n > 0:
        c += 1
        print(f'{n} x {c} = {n * c}')
