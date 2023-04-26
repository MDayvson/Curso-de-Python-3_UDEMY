import random
import tkinter as tk

# palavras para o jogo
palavras = ['python', 'java', 'ruby', 'javascript', 'csharp', 'html', 'css', 'php']

# selecionar uma palavra aleatória
palavra = random.choice(palavras)

# criando a variável que vai guardar as letras adivinhadas
adivinhadas = []

# número de tentativas
tentativas = 6

# criar janela principal
janela = tk.Tk()
janela.title('Jogo da Forca')

# função para atualizar o jogo
def atualiza_jogo():
    # mostrar a palavra com as letras adivinhadas
    palavra_mostrada = ''
    for letra in palavra:
        if letra in adivinhadas:
            palavra_mostrada += letra + ' '
        else:
            palavra_mostrada += '_ '
    label_palavra.config(text=palavra_mostrada)
    
    # checar se o jogador venceu
    if set(palavra) == set(adivinhadas):
        label_resultado.config(text='Você venceu!')
        entry_letra.config(state=tk.DISABLED)
        button_tentar.config(state=tk.DISABLED)
    
    # mostrar quantas tentativas restam
    label_tentativas.config(text=f'Tentativas restantes: {tentativas}')
    
    # checar se o jogador perdeu
    if tentativas == 0:
        label_resultado.config(text=f'Você perdeu! A palavra era: {palavra}')
        entry_letra.config(state=tk.DISABLED)
        button_tentar.config(state=tk.DISABLED)

# função para verificar a letra tentada
def tenta_letra():
    letra = entry_letra.get().lower()
    
    # checar se a letra já foi adivinhada
    if letra in adivinhadas:
        label_resultado.config(text='Você já tentou essa letra.')
    else:
        # adicionar a letra à lista de letras adivinhadas
        adivinhadas.append(letra)
        
        # checar se a letra está na palavra
        if letra in palavra:
            label_resultado.config(text='Acertou!')
        else:
            label_resultado.config(text='Errou!')
            global tentativas
            tentativas -= 1
        
        # atualizar o jogo
        atualiza_jogo()
    
    # limpar a entrada de letra
    entry_letra.delete(0, tk.END)

# criar widgets
label_palavra = tk.Label(janela, font=('Arial', 24))
label_palavra.pack(pady=10)

entry_letra = tk.Entry(janela, font=('Arial', 16))
entry_letra.pack(pady=10)
entry_letra.focus()

button_tentar = tk.Button(janela, text='Tentar', font=('Arial', 16), command=tenta_letra)
button_tentar.pack()

label_tentativas = tk.Label(janela, font=('Arial', 16))
label_tentativas.pack(pady=10)

label_resultado = tk.Label(janela, font=('Arial', 16))
label_resultado.pack(pady=10)

# atualizar o jogo pela primeira vez
atualiza_jogo()

# iniciar a janela principal
janela.mainloop()
