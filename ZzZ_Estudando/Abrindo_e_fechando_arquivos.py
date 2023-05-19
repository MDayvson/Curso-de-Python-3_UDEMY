CAMINHO_DO_ARQUIVO = 'teste.txt'

# escrevendo

with open(CAMINHO_DO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    arquivo.write(input('Nome: ') + '\n')
    arquivo.write(input('Idade: ') + '\n')
    arquivo.write(input('Sexo: ') + '\n')

# lendo

with open(CAMINHO_DO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    for linha in arquivo.readlines():
        print(linha.strip())
