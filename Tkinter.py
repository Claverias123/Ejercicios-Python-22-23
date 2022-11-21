from tkinter import *
from tkinter import ttk

def saludar():
    texto=campoTexto.get()
    textoLabel.set(texto)


#Generar la ventana
ventana = Tk()
ventana.config(background="red")
ventana.geometry("300x500")
ventana.resizable(width=False,height=False)




#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes Laber y Button
textoLabel=StringVar()
textoLabel.set("España>Francia")
labelTexto=ttk.Label(frm, textvariable=textoLabel)
labelTexto.config(background="yellow", border=5, font=("Arial",15))
labelTexto.pack()

#Componente cuadro del texto
campoTexto=ttk.Entry(frm)
campoTexto.pack()



ttk.Button(frm, text="Saludo", command=saludar).pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()



ventana.mainloop()