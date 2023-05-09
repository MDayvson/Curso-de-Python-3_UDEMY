import tkinter as tk

def ler_float(msg):
    while True:
        try:
            n = str(input(msg)).replace(',', '.').strip()
            num = float(n)
        except (TypeError, ValueError):
            print('Digite apenas números.')
            continue
        except (KeyboardInterrupt):
            print('Não digitou.')
            return 0
        else:
            return num


def ler_inteiro(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            print('Digite apenas um número.')
            continue
        except (KeyboardInterrupt):
            print('Não digitou.')
            return 0
        else:
            return num       


def cabeçalho(txt):
    print('-'*32)
    print(txt.center(32))
    print('-'*32)


cabeçalho('CALCULADORA')
while True:
    n1 = ler_float('Número 1: ')
    n2 = ler_float('Número 2: ')

    cabeçalho("""
[1] ADICÃO
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO""")
    
    while True:
        escolha = ler_inteiro('Digite a opção: ')
        if escolha not in (1, 2, 3, 4):
            continue
            
        if escolha == 1:
            print(f'{n1} + {n2} = {n1+n2}')
        elif escolha == 2:
            print(f'{n1} - {n2} = {n1-n2}')
        elif escolha == 3:
            print(f'{n1} * {n2} = {n1*n2}')
        elif escolha == 4:
            if n2 == 0:
                print('Não pode divisão por ZERO')
            else:
                print(f'{n1} / {n2} = {n1/n2}')
        break

    while True:
        opc = input('Quer continuar: [S/N] ').strip().upper()[0]
        if opc in 'SN':
            break
    if opc == 'N':
        break
print('FIM')




