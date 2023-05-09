def multiplicar(*args):
    total = 1
    for numero in args:
        if numero == 0:
            continue
        else:
            total *= numero
    return total


def par_impar(num):
    if num % 2 == 0:
        return 'Par'
    return 'Impar'


resultado = multiplicar(0,5,0,5)
print(resultado)

resposta = par_impar(1)
print(f'O número é {resposta}')
