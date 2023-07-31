from time import sleep
def contador(inicio, fim, passo):
    print(f'contagem de {inicio} até {fim} de {passo} em {passo}')
    '''for i in range(inicio,fim,passo):
        print(f'{i} ', end='')
        sleep(1)
    print('fim')'''
    if passo < 0:
        passo *= -1
    if inicio< fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            #sleep(0.5)
            cont += passo
        print('fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            #sleep(0.5)
            cont -= passo
        print('fim')


contador(1, 11, 1)
contador(10, 0, -2)
ini = int(input('digite o inicio'))
fi = int(input('digite o fim'))
pas = int(input('digite o passo'))
contador(ini,fi ,pas )