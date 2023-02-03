n1 = float(input('digite uma nota '))
n2 = float(input('digite outra nota '))
m = (n1 + n2) / 2
if m < 5.0:
    print('\033[41mREPROVADO\033[m')
elif m <= 6.9: # m >5 and m <7 ou >7 m >= 5
    print('\033[43mRECUPERAÇÃO\033[m')
else:
    print('\033[42mAPROVADO\033[m')
