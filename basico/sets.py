# ----- sets -----
# un set no es una estructura ordenada, no se puede acceder a los elementos segun su index
# no admite repetidos

mi_set = set()
print(type(mi_set)) # class 'set'
mi_otro_set ={}
print(type(mi_otro_set)) # class 'dict'

mi_otro_set = {1.7,35,"Maxi"}
print(type(mi_otro_set)) # class 'set'

print(len(mi_otro_set))
mi_otro_set.add("Riftan")
print(mi_otro_set) # esta desordenado
mi_otro_set.add("Maxi")
print(mi_otro_set) # no contiene duplicados
print("Maxi" in mi_otro_set)
print("maxi" in mi_otro_set)
mi_otro_set.remove(35)
print(mi_otro_set)
 
mi_otro_set.clear() # vacia el set, pero sigue existiendo
print(mi_otro_set) # set()
print(len(mi_otro_set)) # 0
del mi_otro_set # lo elimina 
#print(mi_otro_set) no esta definido

mi_set_tres = {1.7,35,"Maxi"}
mi_lista = list(mi_set_tres)
print(mi_lista[0]) # al no estar ordenado el set, no tenemos control sobre como se crea la lista

set_uno = {1,2,3}
set_dos = {"uno", "dos", "tres"}
# set_suma = set_uno + set_dos no existe
set_suma= set_uno.union(set_dos)
print(set_suma)
print(set_suma.union({"cuatro, 4"}))
print(set_suma)

set_tres = {"Harry", "Hermione", "Ron" , "Fred", "George"}
set_cuatro = {"Harry", "Hermione", "Ron" , "Draco", "Luna"}
print(set_tres.difference(set_cuatro))
print(set_cuatro.difference(set_tres))