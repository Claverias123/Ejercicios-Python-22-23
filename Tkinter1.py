from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usu=""
contr=""
confir=""
vLista=[]

def GUARDAR():
    usu=datosUsuario.get()
    contr=datosContraseña.get()
    confir=datosConfirmacion.get()
    if contr==confir:
        vLista.append(usu)
        vLista.append(contr)
        datosUsuario.delete(0,len(usu))
        datosContraseña.delete(0,len(contr))
        datosConfirmacion.delete(0,len(confir))
        messagebox.showinfo("Usuario Guardado", f"Usuario {usu} guardado correctamente :)")
        
 


#Generar la ventana
ventana = Tk()
ventana.title("Datos Registro")
ventana.geometry("400x300")
ventana.config(background="palegreen")
ventana.resizable(False,False)

labelTitulo=ttk.Label(ventana, text="DATOS PERSONALES:")
labelTitulo.config(background="palegreen")
labelTitulo.grid(row=0,column=1,pady=10)

datosUsuario= ttk.Entry(ventana)
datosUsuario.grid(row=1,column=1,pady=10)

labelUsuario=ttk.Label(ventana, text="Usuario:")
labelUsuario.config(background="palegreen")
labelUsuario.grid(row=1,column=0,pady=10)

datosContraseña= ttk.Entry(ventana,show="****")
datosContraseña.grid(row=2,column=1,pady=10)

labelContraseña=ttk.Label(ventana, text="Contraseña:")
labelContraseña.config(background="palegreen")
labelContraseña.grid(row=2,column=0,pady=10)

datosConfirmacion= ttk.Entry(ventana,show="****")
datosConfirmacion.grid(row=3,column=1,pady=10)

labelConfirmacion=ttk.Label(ventana, text="Confirmar contraseña:")
labelConfirmacion.config(background="palegreen")
labelConfirmacion.grid(row=3,column=0,pady=10)

salir=ttk.Button(ventana, text="Salir", command=ventana.destroy)
salir.grid(row=4,column=1,pady=10)

botonGuardar=ttk.Button(ventana, text="Guardar", command=GUARDAR)
botonGuardar.grid(row=4,column=0,pady=10)

ventana.mainloop()