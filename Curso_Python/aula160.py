# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy


def imprimir_lista(lista):
    for produto in lista:
        for k, v in produto.items():
            print(f'{k}: {v}',end='  ')
        print('')
    

def titulo(msg):
    print('='*40)
    print(msg)
    print('='*40)


titulo('produtos')
imprimir_lista(produtos)

# 1 
titulo('Produtos com aumento de 10%')
novos_produtos = [{**produto, 'preco':round(produto['preco'] * 1.1, 2)} 
                  for produto in copy.deepcopy(produtos)]
imprimir_lista(novos_produtos)


# 2 
titulo('Produtos ordenado por nome decrescente')
produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), 
                                     key = lambda iten: iten['nome'], 
                                     reverse= True)
imprimir_lista(produtos_ordenados_por_nome)



# 3
titulo('Produtos ordenados por preço')
produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), 
                                      key = lambda iten: iten['preco'])
imprimir_lista(produtos_ordenados_por_preco)