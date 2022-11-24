from tkinter import *
from tkinter import ttk

def GUARDAR():
    text=datosUsuario.get()
    print("Usuario:", text)
    text2=datosContraseña.get()
    print("Contraseña:", text2)


#Generar la ventana
ventana = Tk()
ventana.title("Datos personales")
ventana.geometry("325x200")
ventana.config(background="palegreen")
ventana.resizable(False,False)

labelTitulo=ttk.Label(ventana, text="DATOS PERSONALES:")
labelTitulo.config(background="palegreen")
labelTitulo.grid(row=0,column=1)

datosUsuario= ttk.Entry(ventana)
datosUsuario.grid(row=1,column=1)

labelUsuario=ttk.Label(ventana, text="Usuario:")
labelUsuario.config(background="palegreen")
labelUsuario.grid(row=1,column=0)

datosContraseña= ttk.Entry(ventana)
datosContraseña.grid(row=2,column=1)

labelContraseña=ttk.Label(ventana, text="Contraseña:")
labelContraseña.config(background="palegreen")
labelContraseña.grid(row=2,column=0)

salir=ttk.Button(ventana, text="Salir", command=ventana.destroy)
salir.grid(row=100,column=0)

botonGuardar=ttk.Button(ventana, text="Guardar", command=GUARDAR)
botonGuardar.grid(row=100,column=10)

ventana.mainloop()