# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
import string
from datetime import datetime
from pathlib import Path


locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = locale.currency(numero, symbol=True, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

print(dados)


class MyTemplate(string.Template):  # usado para mudar o delimitador
    # delimiter = '%'
    ...


texto = '''

Ola, $nome

O valor de $valor de estará disponivel para retirada em $data.
Depositado pela $empresa, qualquer duvida ligue para $telefone.

'''

template = string.Template(texto)
print(template.substitute(dados))


# pode vir de um arquivo txt externo.

# CAMINHO_ARQUIVO = Path(__file__).parent / 'aula298.txt'
# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     texto = arquivo.read()
#     template = MyTemplate(texto)
#     print(template.substitute(dados))
