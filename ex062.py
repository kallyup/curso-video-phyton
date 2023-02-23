a1 = int(input('primeiro termo da pa '))
r = int(input('razão da pa '))
pa = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while pa <= total:
        print(a1)
        a1 += r
        pa += 1
    print('pausa')
    mais = int(input('quantos termos vc quer'))
print('fim')
print(pa)
