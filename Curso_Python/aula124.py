perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return None
        else:
            return n
        

tot_perguntas = 0
acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    tot_perguntas += 1
    
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}) {opcao}')

    while True:
        opc = leiaint('Escolha uma opção: ')
        if 0 <= opc <= len(pergunta['Opções']):
            break
        else:
            print(f'Digite um número entre 0 e {len(pergunta["Opções"])-1}')

    if pergunta['Opções'][opc] == pergunta['Resposta']:
        print('Acertou')
        acertos += 1
    else:
        print('Errou')

print(f'Voçê acertou {acertos} de {tot_perguntas} perguntas.')
