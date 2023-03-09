meses = int(input('quantos meses de experiência em sala você possui? '))
publi = int(input('quantas publicações você possui nos ultimos 2 anos?'))

if meses < 60 or publi < 3:
    print('não atende')
else:
    print('atende')
