import os
import shutil
from pathlib import Path
################################################################
# 1 forma

HOME = os.path.expanduser('~')
print(f'Raiz do sistema >>> {HOME}')
DESKTOP = os.path.join(HOME, 'DESKTOP')
print(f'Endereço do Desktop >>> {DESKTOP}')
caminho_da_pasta = os.path.join(DESKTOP, 'Nova_Pasta')
print(f'Caminho da pasta >>> {caminho_da_pasta}')
################################################################
# Outra forma de pegar o caminho

CAMINHO_DA_PASTA = Path.home() / 'Desktop' / 'Nova Pasta'
CAMINHO_DA_PASTA.mkdir(exist_ok=True)  # criando pasta
SUBPASTA = CAMINHO_DA_PASTA / 'Subpasta'
SUBPASTA.mkdir(exist_ok=True)  # criando subpasta
################################################################

# Criando a pasta

pasta = Path(caminho_da_pasta)
pasta.mkdir(exist_ok=True)  # cria a pasta

shutil.rmtree(pasta, ignore_errors=True)  # apaga a pasta


################################################################
# movendo a pasta

origem = CAMINHO_DA_PASTA  # pasta de origem

caminho_do_projeto = Path()  # pega o caminho do projeto
caminho_do_projeto.absolute()

caminho_do_arquivo = Path(__file__)
print(f'Caminho do projeto >>>{caminho_do_arquivo}')
# usanso .paraent, pega niveis acima
# ex: caminho_do_projeto.parent

destino = caminho_do_arquivo.parent
print(f'Destino >>> {destino}')

shutil.move(origem, destino)
