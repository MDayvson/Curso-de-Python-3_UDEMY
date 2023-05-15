import datetime
pessoa = {}
lista = []


def leiavirgula(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! "{entrada}" é um valor invalido\033[m')
        else:
            valido = True
            return float(entrada)


while True:
    pessoa['nome'] = str(input('Nome: ')).strip().title()
    pessoa['sobrenome'] = str(input('Sobrenome: ')).strip().title()
    pessoa['ano_nascimento'] = int(input('Ano de nascimento: ').strip())
    ano_atual = datetime.datetime.now().year
    pessoa['idade'] = ano_atual - pessoa['ano_nascimento']
    pessoa['altura'] = leiavirgula('Altura: ')

    lista.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print('Digite S ou N: ')
    if resp == 'N':
        break
print('-='*30)
for p in lista:
    for k, v in p.items():
        print(f'{k}: {v}')
    print('-='*30)
