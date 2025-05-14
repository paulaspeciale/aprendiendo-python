# ----- tuplas -----
# tupla -> conjunto de valores, no mutables
mi_tupla = tuple()
mi_otra_tupla = () 
otra_tupla =(1,2,3)
mi_tupla = (35,1.77,"Maxi",35)
print(mi_tupla)
print(type(mi_tupla))
print(mi_tupla[0]) #35
print(mi_tupla[-1]) # Maxi
print(mi_tupla[4]) # Error -> index out of range
print(mi_tupla.count(35))
print(mi_tupla.index(1.77))
print(mi_tupla.index(35)) # 0 , el primero
# mi_tupla[0] = 1.60 error -> tuple does not support item assigment
print(mi_tupla + otra_tupla)
mi_tupla_sumada = mi_tupla + otra_tupla
# slices
print(mi_tupla[1:4])

mi_lista_tuple = list(mi_tupla)
print(type(mi_lista_tuple))
mi_lista_tuple[0] = 20
mi_lista_tuple.index(0,"Blue")
print(mi_lista_tuple)
tuple(mi_lista_tuple)