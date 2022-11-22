#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Importamos tkinter, os y sys para poder recibir el video desde la linia de comandos. 
import tkinter as tk 
from tkinter import ttk as ttk
import os
import sys

#El video a convertir es el primer y unico parametro de entrada.
video = sys.argv[1]

# A continuación se definen las funciones de conversion a cada formato de codificación:
# Todas ellas tienen como input el video original.
# Se ejecuta en la linia de comandos la conversion mediante ffmpeg a los respectivos formatos.

def h265(video):
    try:
        command = "ffmpeg -i " + video + " -c:v libx265 -preset slow -crf 20 h265.mp4"
        os.system(command)
    except:
        print('El video que deseas codificar no es válido.')
        
def vp8(video):
    try:
        command = "ffmpeg -i " + video + " -c:v libvpx -b:v 1M vp8.webm"
        os.system(command)
    except:
        print('El video que deseas codificar no es válido.')

def vp9(video):
    try:
        command = "ffmpeg -i " + video + " -c:v libvpx-vp9 -b:v 2M vp9.webm"
        os.system(command)
    except:
        print('El video que deseas codificar no es válido.')

def av1(video):
    try:
        command = "ffmpeg -i " + video + " -c:v libaom-av1 -strict -2 -crf 30 av1.mp4"
        os.system(command)
    except:
        print('El video que deseas codificar no es válido.')

def play(event):
    try:
        command = 'ffmpeg -i vp9.webm -i vp8.webm -i h265.mp4 -i output.mp4 -filter_complex "[0:v][1:v][2:v][3:v]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" quatro.mp4'
        os.system(command)
        command2 = 'ffplay quatro.mp4'
        os.system(command2)
    except:
        print('No s epuede reprducir el video.')

# Se inicializa el Tk
root = tk.Tk()

root.title("Conversor de videos") # Titulo de la ventana

root.geometry("380x400") # Tamaño de la ventana

#Iniciamos los botones con su texto, con pack entran en el root, y finalmente les assignamos la funcion que realizaran

bvp8 = ttk.Button(root, text="Codificar video con vp8")
bvp8.pack()
bvp8.bind("<ButtonPress-1>", vp8(video))

bh265 = ttk.Button(root, text="Codificar video con h265")
bh265.pack()
bh265.bind("<ButtonPress-1>", h265(video))

bvp9 = ttk.Button(root, text="Codificar video con vp9")
bvp9.pack()
bvp9.bind("<ButtonPress-1>", vp9(video))

bav1 = ttk.Button(root, text="Codificar video con av1")
bav1.pack()
bav1.bind("<ButtonPress-1>", av1(video))

bshow = ttk.Button(root, text="Mostrar los videos convertidos")
bshow.pack()
bshow.bind("<ButtonPress-1>", play)

# Se activa la ventana del TK
root.mainloop()



# In[ ]:





# In[ ]:




