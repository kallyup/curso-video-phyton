'''num = int(input('digite um numero '))
c = num
while c != 1:
    c = c - 1
    num = num * c
print(num)
'''
'''num = int(input('digite um numero '))
res = 1
c = 1
while c <= num:
    res *= c
    c += 1
print(c)
print(res)'''

'''from math import factorial
n = int(input('digite um numero'))
f = factorial(n)
print(f)'''
n = int(input('digite um valor'))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print("x" if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
