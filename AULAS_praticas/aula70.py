letra_mais_vezes = ''
qtd_letra_mais_apareceu = 0


while True:
    frase = input('Digite uma frase: ').upper().strip()

    i = 0
    while i < len(frase):
        letra_atual = frase[i]

        if letra_atual == ' ':
            i += 1
            continue

        qtd_letra_atual = frase.count(letra_atual)

        if qtd_letra_atual > qtd_letra_mais_apareceu:
            qtd_letra_mais_apareceu = qtd_letra_atual
            letra_mais_vezes = letra_atual
        
        i += 1
    break

print(f'A letra que mais apareceu foi {letra_mais_vezes}, total de {qtd_letra_mais_apareceu}x')
