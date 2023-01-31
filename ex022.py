'''frase = 'curso em video python'
print(frase[:13])
print(frase[2:17:3])
print(frase[1::2])
print(frase.count('r'))
print(frase.upper())
print(len(frase.strip()))
print(frase.replace('python', 'android'))
print(("curso" in frase))
print(frase.lower().find(('video')))
print(frase.split())'''

n = str(input('digite seu nome: ')).strip()
print(n.lower())
print(n.upper())
print(len(n) - n.count(' '))
#print(n.find(' '))
separa = n.split()
print(len(separa[0]))