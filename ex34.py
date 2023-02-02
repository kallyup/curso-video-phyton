s = float(input('qual seu salario? '))
if s > 1250:
    print('\033[7;40m{:.2f}\033[m'.format(s*1.1))
else:
    print('\033[4;32;45m{:.2f}\033[m'.format(s * 1.5))
