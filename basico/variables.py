#nombrando variables -> snakecase
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
'''
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print("Tu nombre es:", nombre, "Tu edad es", edad)
'''
#tipado débil
address: str = "mi direccion"
print("address: str",type(address))
address = 32
print(type(address))

prueba_number: int = 3+2j
print("forzamos el tipo int:" , type(prueba_number))