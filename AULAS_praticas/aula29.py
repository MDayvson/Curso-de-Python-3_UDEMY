# Calculo IMC

def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiavirgula(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print('ERRO')
        else:
            valido = True
            return float(entrada)
        

nome = input('Nome: ').strip().title()
altura = leiavirgula('Altura: ')
peso = leiavirgula('Peso: ')

imc = peso / (altura * altura)

cabeçalho('Calculo do IMC')
print(f'{nome} tem {altura} de altura'),
print(f'pesa {peso}kg e seu IMC é {imc:.2f}')
print(linha())
