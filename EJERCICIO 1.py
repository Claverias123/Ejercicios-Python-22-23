from tkinter import *
from tkinter import ttk

#Generar la ventana
ventana = Tk()
ventana.config(background="chartreuse")
ventana.geometry("300x500")
ventana.resizable(width=False,height=False)
ventana.PhotoImage(file=("perro.png"))


#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes Laber y Button
labelTexto=ttk.Label(frm, text="Hola mesi")
labelTexto.config(background="deep pink", border=5, font=("Arial",15))
labelTexto.pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()