import random
def diferenca(array1, array2):
    c = l = 0
    min = float('inf')
    resultadoPar = None
    while c < len(array1) and l < len(array2):
        dif = abs(array1[c] - array2[l])
        if dif < min:
            min = dif
            resultadoPar = {'valor1': array1[c], 'valor2': array2[l], 'diferença': min}
        if array1[c] < array2[l]:
            c += 1
        else:
            l += 1
    return resultadoPar
array1 = [random.randint(1,60) for i in range(0,6)]
array2 = [random.randint(1,60) for i in range(0,6)]
resultado = diferenca(array1, array2)
print(resultado)
