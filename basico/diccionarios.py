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
print(mi_otro_diccionario["1"]) #error
print(mi_otro_diccionario[1]) 



