'''
1-Insertar contacto
2- Borra contacto
3- Buscar contacto
4- Ver todos los contactos
5- Salir
'''
def pintaMenu():
    vNom=[]
    vTlf=[]
    opc=0
    while (opc<1 or opc>5):
        print("1-Insertar contacto")
        print("2- Borra contacto")
        print("3- Buscar contacto")
        print("4- Ver todos los contactos")
        print("5- Salir")
        print("************************")
        try:
            opc= int(input("Seleccione una opción\n"))
        except:
            print("Las opciones son de la 1 al 5")
    return opc



opc=pintaMenu()      


