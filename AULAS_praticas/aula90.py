import os

lista = []

while True:
    opc = input('[i]nserir, [a]pagar, [l]istar: ').strip().upper()

    if opc not in 'IAL':
        print('Escolha I, A ou L')
        
    if opc == 'I':
        os.system('cls')
        lista.append(input('Valor: '))

    elif opc == 'A':
        if len(lista) == 0:
            print('Lista vazia')
            continue
            
        try:
            indice = input('Escolha o indice para apagar: ')
            indice = int(indice)
            print(f'{lista[indice]} apagado com sucesso.')
            lista.pop(indice)
        except:
            print('Não esta na lista')
            
    elif opc == 'L':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar')
            
        else:
            for i, v in enumerate(lista):
                print(f'{i} {v}')
