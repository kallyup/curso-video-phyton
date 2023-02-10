num = int(input('digite um numero: '))
primo = 0
for c in range(1, num+1):
    if num % c == 0:
        primo += 1
if primo == 2:
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')


