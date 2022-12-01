from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usu=""
contr=""
confir=""
sexo=""
vLista=[]

def GUARDAR():
    usu=datosUsuario.get()
    contr=datosContraseña.get()
    confir=datosConfirmacion.get()
    sexo=datosDesplegable.get()
    if contr==confir:
        print("Nombre del usuario:", usu)
        print("Contraseña:", contr)
        print("Sexo:", sexo)
        vLista.append(usu)
        vLista.append(contr)
        vLista.append(confir)
        vLista.append(sexo)
        datosUsuario.delete(0,len(usu))
        datosContraseña.delete(0,len(contr))
        datosConfirmacion.delete(0,len(confir))
        datosSexo.delete(0,len(sexo))

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

datosSexo= ttk.Entry(ventana)
datosSexo.grid(row=4,column=1,pady=10)
datosDesplegable=ttk.Combobox(ventana,state="readonly",values=["Hombre","Mujer","No binario"])
datosDesplegable.grid(row=4,column=1,pady=10)
datosDesplegable.set("Dime su sexo")


labelSexo=ttk.Label(ventana, text="Sexo:")
labelSexo.config(background="palegreen")
labelSexo.grid(row=4,column=0,pady=10)

salir=ttk.Button(ventana, text="Salir", command=ventana.destroy)
salir.grid(row=5,column=1,pady=10)

botonGuardar=ttk.Button(ventana, text="Guardar", command=GUARDAR)
botonGuardar.grid(row=5,column=0,pady=10)

ventana.mainloop()