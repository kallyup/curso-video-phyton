from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('digite o nome'))
nasicmento = int(input('digite o ano de nascimento'))
pessoa['idade'] = datetime.now().year - nasicmento
pessoa['carteira'] = int(input('digite o numero da carteira de trabalho'))
if pessoa['carteira'] == 0:
    for k, v in pessoa.items():
        print(f'  -{k} tem valor {v}')
else:
    pessoa['contratação'] = int(input('ano de contratação'))
    pessoa['salario'] = float(input('qual salario'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 40) - datetime.now().year)
    for k, v in pessoa.items():
        print(f'  -{k} tem valor {v}')

