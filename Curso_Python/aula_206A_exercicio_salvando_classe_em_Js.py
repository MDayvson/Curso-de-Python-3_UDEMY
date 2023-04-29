# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Merari', 35)
p2 = Pessoa('Ana', 16)
p3 =Pessoa('Helena', 21)

bd = [p1.__dict__, vars(p2), vars(p3)]  # Pode usar tanto o __dict__ quanto o vars

CAMINHO_ARQUIVO = 'aula206.json'

with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=4)
