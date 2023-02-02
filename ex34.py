s = float(input('qual seu salario? '))
if s >1.250:
    print('{:.2f}'.format(s*1.1))
else:
    print('{:.2f}'.format(s * 1.5))
