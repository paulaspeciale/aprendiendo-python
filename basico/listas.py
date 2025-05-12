# estructura de datos
mi_lista = list()
mi_otra_lista = []
print(len(mi_lista)) # 0

mi_lista = [35,24,62,52,60,30,30,17,25,30]
print(mi_lista)
print(len(mi_lista))
mi_otra_lista = [39,1.63,"Evangelina"]

print(type(mi_lista)) # <class 'list'>
print(mi_lista[0]) # primer elemento
print(mi_lista[-1]) # último elemento
#print(mi_otra_lista[3]) # index error - index out of range
print(mi_lista.count(30)) # 3 hay 3 30 en mi_lista

edad,altura, nombre = mi_otra_lista # necesita que se utilicen todos los elementos, si quitara nombre por ejemplo fallaría

#concatenación de listas
print(mi_otra_lista + mi_lista)
mi_otra_lista.append("Trystan")
print(mi_otra_lista)
mi_otra_lista.insert(1, "Purpura") # no reemplaza el valor, corre los demas
print(mi_otra_lista)

mi_otra_lista.remove("Purpura")
mi_lista.remove(30) #solo elimina uno
print(mi_lista.pop()) # elimina el ultimo y lo devuelve
mi_lista.pop(2)
mi_otra_lista[0] =  55

mi_nueva_lista = mi_lista.copy()
mi_lista.clear()
print(mi_lista) # esta vacía
print(mi_nueva_lista) # contiene todos los elementos, es un objeto nuevo
mi_nueva_lista.reverse() # altera la lista original
print(mi_nueva_lista)
mi_nueva_lista.sort() # podemos agregar criterios de ordenación 