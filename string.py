def mudanca1(s1, s2):
    comp = abs(len(s1) - len(s2))
    if comp > 1:
        return False
    cort = s1
    lon = s2 \
        if len(s1) <= len(s2) \
        else (s2, s1)
    c = l = edit = 0
    while c < len(cort) and l < len(lon):
        if cort[c] != lon[l]:
            edit += 1
            if edit > 1:
                return False
            if comp == 1:
                l += 1
            else:
                c += 1
                l += 1
        else:
            c += 1
            l += 1
    if comp == 1:
        edit += 1
    return edit == 1
cont = 'S'.upper()
while cont == 'S':
    print(mudanca1(s1 = str(input('digite a palavra')), s2 = str(input('digite a palavra com ou sem alterações'))))
    cont = str(input('quer continuar S ou N? ')).upper()
    while True:
        if cont == 'N':
            break
        elif cont != 'S':
            print('digite um valor valido')
            cont = str(input('quer continuar S ou N? ')).upper()
        else:
            break
