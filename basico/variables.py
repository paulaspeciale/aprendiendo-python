# ----- Variables -----
# Una variable se crea cuando se le asigna un valor.
'''
Reglas para nombrar variables

    El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo)
    El nombre de la variable debe comenzar con una letra;
    El carácter guion bajo es considerado una letra;
    Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el mundo real - Alicia y ALICIA son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes);
    El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python (las palabras clave - explicará más de esto pronto).

'''
'''
ejemplos de nombres de variables ilegales
101
m 101
del

'''
#nombrando variables -> snakecase
print(Var) # name Var is not defined
my_string_variable = "My string variable"
print(my_string_variable)
my_int_variable = 3
print(my_int_variable)
my_bool_variable = True
print(my_bool_variable)
#print con varios argumentos
print(my_bool_variable,my_int_variable,my_string_variable) # creo una cadena con todas las variables 

# conversion de tipos de datos
my_string_to_int = int("5")
print("string to int ->", type(my_string_to_int))
my_int_to_string = str(4)
print("int to string ->", type(my_int_to_string))

#variables en una sola linea
name, surname, age = "Riftan", "Calypse", 28
print(name)
print(age)
print(surname)
# no es una buena práctica

#tipado débil
address: str = "mi direccion"
print("address: str",type(address))
address = 32
print(type(address))

prueba_number: int = 3+2j
print("forzamos el tipo int:" , type(prueba_number))