import json

CAMINHO_DO_ARQUIVO = 'teste2.json'


pessoa = {
    'nome': 'Merari',
    'sobrenome': 'Dayvson',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open(CAMINHO_DO_ARQUIVO, 'w', encoding= 'utf8') as arquivo:
    json.dump(pessoa, arquivo, indent= 2, ensure_ascii= False)