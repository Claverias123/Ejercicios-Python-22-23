#Listas en python

vNom=[]

#Insertar un dato
vNom.insert(0,"Cabe")
vNom.insert(1,"Martos")
vNom.insert(2,"Manza")
vNom.append("Rufino")

#Eliminar elementos de lista
vNom.remove("Martos")
NomBorrado=vNom.pop(2)
print("El nombre borrado es", NomBorrado)

#Ordenar una lista
vNom.sort(reverse=True)

#Contar el número de elementos de la lista
print(vNom.count("Manza"))
print("La lista tiene",len (vNom))


print(vNom)