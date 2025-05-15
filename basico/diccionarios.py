# ----- diccionarios -----

mi_diccionario = dict()
mi_otro_diccionario = {}
print(mi_diccionario)
print(type(mi_diccionario)) # class 'dict'
mi_otro_diccionario = {
    "nombre" : "Maxi",
    "apellido" : "Calypse",
    "edad" : 22,
    "ocupaciones" : {"Lady", "Maga"},
    1:1.75
}
print(mi_otro_diccionario["ocupaciones"])
#print(mi_otro_diccionario["1"]) #error
print(mi_otro_diccionario[1]) 

mi_diccionario_temporal = {
    "Hola" : "voy a ser eliminado",
    "calle" : "221b baker street"

}
del mi_diccionario_temporal["calle"]

print("Maxi" in mi_otro_diccionario) # de esta farma busca por clave, no por valor
print("edad" in mi_otro_diccionario)

print(mi_otro_diccionario.items()) # listado de cada uno de los items
print(mi_otro_diccionario.keys())
print(mi_otro_diccionario.values())

mi_nuevo_diccionario = mi_otro_diccionario.fromkeys(("Nombre",1))
print(mi_nuevo_diccionario)

mi_diccionario_temporal = dict.fromkeys(("Nombre",1,"piso"))
print(mi_diccionario_temporal)
mi_nuevo_nuevo_diccionario = dict.fromkeys(mi_otro_diccionario)
print(mi_nuevo_nuevo_diccionario)

mi_nuevo_nuevo_diccionario = dict.fromkeys(mi_otro_diccionario,("Nombre", "Apellido"))
print(mi_nuevo_nuevo_diccionario)
mi_nuevo_nuevo_diccionario = dict.fromkeys(mi_otro_diccionario, "valor por defecto para todas las claves")
print(mi_nuevo_nuevo_diccionario)

print(list(mi_otro_diccionario)) #transforma en una lista las claves
print(tuple(mi_otro_diccionario)) 
print(set(mi_otro_diccionario)) 


