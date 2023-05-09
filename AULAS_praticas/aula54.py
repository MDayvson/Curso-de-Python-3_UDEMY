"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def leia_inteiro(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Esse número não é inteiro, digite um número inteiro.')
            continue
        except (KeyboardInterrupt):
            print('O usuario não digitou um número.')
            return 0
        else:
            return n


num = leia_inteiro('Digite um número inteiro: ')
if num % 2 == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é IMPAR.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = leia_inteiro('Digite a Hora: ')
if 0 <= hora <= 11:
    print('BOM DIA')
elif 12 <= hora <= 17:
    print('BOA TARDE')
elif 18 <= hora <= 23:
    print('BOA NOITE')
else:
    print('Não conheço essa hora.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = str(input('Digite seu primeiro nome: ')).strip().title()
if len(nome) > 1:
    if len(nome) <= 4:
        print('Seu nome é curto.')
    elif 5<= len(nome) <=6:
        print('Seu nome é normal.') 
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite mais de uma letra.')
