'''
Opción 1:
Lista para nombre
Lista para números

Opción 2:
Lista para nombres y teléfonos
Ejemplo [Arturo - Teléfono, Pedro - Teléfono]
'''

#Opción 1
from re import I


vNom=[]
vTel=[]

nom=input("Dime un nombre\n")
tel=input("Dime un número\n")

vNom.append(input("Dime tu nombre"))
vTel.append(input("Dime tu teléfono"))

print("Número de telefono de ", nom, "es", tel)
print("Número de telefono de ", vNom.pop, "es", vTel.pop)


#Bucle while
i=0
while(True):
    print("No hagas esto nunca", i)
    i=i+1