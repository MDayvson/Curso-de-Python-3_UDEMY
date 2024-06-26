import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
import threading
import math
from turtle import speed, bgcolor, goto, color, done
import pygame
import pathlib

pygame.init()

root = tk.Tk()
root.title('Aceitas?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


# # Carregar imagem para o papel de parede
# from PIL import Image, ImageTk
# wallpaper_path = pathlib.Path(__file__).parent / 'wallpaper.jpg'
# wallpaper_image = Image.open(wallpaper_path)
# wallpaper_photo = ImageTk.PhotoImage(wallpaper_image)

# # Configurar o papel de parede
# background_label = Label(root, image=wallpaper_photo)
# background_label.place(relwidth=1, relheight=1)


# caminho da música
CAMINHO_MUSICA = pathlib.Path(__file__).parent / 'Forever Star.mp3'
pygame.mixer.music.load(CAMINHO_MUSICA)

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 50:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo('Meu amor', 'Eu te amo meu amor, Ouça a musica.')
    threading.Timer(1, draw_heart).start()  # Aguarda 1 segundo antes de chamar a função draw_heart

def denied():
    button_1.destroy()
    error_message()

def error_message():
    messagebox.showerror('Erro', 'Desculpe, você clicou na opção errada por engano. Tente novamente.')

def draw_heart():
    pygame.mixer.music.play()  # Inicia a reprodução da música
    speed(0)
    bgcolor('black')
    for i in range(100000):
        goto(hearta(i)*20, heartb(i)*20)
        for j in range(5):
            color('#f73487')
        goto(0, 0)
    done()

def hearta(k):
    return 12*math.sin(k)**3

def heartb(k):
    return 12*math.cos(k)-5 *\
        math.cos(2*k)-2 *\
        math.cos(3*k) -\
        math.cos(4*k)

margin = Canvas(root, width=500, bg='#ffc8dd', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text='Quer namorar comigo?', fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied, relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE, bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()

root.mainloop()
