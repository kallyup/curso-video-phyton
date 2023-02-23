n = int(input('quantos termos vc quer mostrar '))
t1 = 0
t2 = 1
c = 3
while c <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    c += 1
print('fim')
