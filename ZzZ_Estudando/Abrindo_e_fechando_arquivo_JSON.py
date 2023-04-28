import json

CAMINHO_DO_ARQUIVO = 'teste2.json'

pessoa = {}
cadastro = []
while True:

    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
    cadastro.append(pessoa.copy())
    pessoa.clear()

    resp = input('Continuar? ')
    if resp in 'Nn':
        break

# Escrevendo no JSON

with open(CAMINHO_DO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(cadastro, arquivo, ensure_ascii=False, indent=4)

# Lendo do JSON

with open(CAMINHO_DO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    cadastro = json.load(arquivo)
    for pessoa in cadastro:
        print(f'Nome: {pessoa["nome"]}')
        print(f'Idade: {pessoa["idade"]}')
        print(f'Sexo: {pessoa["sexo"]}')