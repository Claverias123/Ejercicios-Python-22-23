from tkinter import *
from tkinter import ttk

from pytube import YouTube
from pytube import Playlist


def descargaCancion():
    url=datosEntrada.get()
    youtube=YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

#Generar la ventana
ventana = Tk()
ventana.title("Descarga tu música desde YT")
ventana.geometry("500x200")
ventana.config(background="deep pink")
ventana.resizable(False,False)

datosEntrada= ttk.Entry(ventana)
datosEntrada.place(x=163,y=25)

botonDescarga=ttk.Button(ventana, text="Descargar canción", command=descargaCancion)
botonDescarga.place(x=180,y=90)

labelTitulo=ttk.Label(ventana, text="Introduce la url de la cancion")
labelTitulo.config(background="pink")
labelTitulo.place(x=150,y=5)

salir=ttk.Button(ventana, text="Salir", command=ventana.destroy)
salir.place(x=205,y=120)

ventana.mainloop()










