'''
1-Insertar contacto
2- Borra contacto
3- Buscar contacto
4- Ver todos los contactos
5- Salir
'''
vNom=[]
vTlf=[]
opc=0
while (opc!=5):
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




    opc=int(input("Dime que hacer\n"))
    if(opc==5):
        print("Has salido de la agenda")