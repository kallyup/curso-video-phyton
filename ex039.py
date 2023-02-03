'''nascimento = int(input('digite o ano de nascimento '))
alistamento = 2023 - nascimento
if alistamento <18:
    print('ainda falta {} anos'.format(18 - alistamento))
elif alistamento < 24:
    print('esta na epoca do alistamento')
else:
    print('ja passaram {} anos do alistamento'.format(alistamento - 24))'''
from  datetime import date
atual = date.today().year
nasc = int(input(('ano de nascimento: ')))
idade = atual - nasc
print(('quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual)))
if idade == 18:
    print('vc tem q se alitar')
elif idade < 18:
    saldo = 18 - idade
    print('anda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('seu alstamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('vc já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi {}'.format(ano))
