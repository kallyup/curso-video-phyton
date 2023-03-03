
from random import randint



c = 0
while True:
    jogador = int(input('digite um numero'))
    comp = randint(0, 10)
    result = (jogador + comp)
    escolha = " "
    while escolha not in "PpIi":
        escolha = str(input('Escolha Par ou Impar [Pp/Ii]')).strip().upper()
    print(f'vc jogou {jogador} e o computador jogou {comp} o toal foi {result}')
    print("deu par" if result %2 == 0 else 'deu impar')
    if escolha == 'P':
        if result % 2 == 0:
            print('vc venceu')
            c += 1
        else:
            print('vc perdeu')
            break
    elif escolha == "I":
        if result % 2 == 1:
            print('vc venceu')
            c += 1
        else:
            print('vc perdeu')
            break
    print('vamos jogar novMENTE')
print(f'vc venceu {c} vezes')
