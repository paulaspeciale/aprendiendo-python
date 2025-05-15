# ----- La función input -----
# La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.
# obtiene los datos de la consola
# el resultado de la función input() es una cadena.
# cuando input() es llamada, el flujo del programa se detiene hasta que el usuario haya ingresado un dato y/o haya presionado la tecla enter
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
print("Tu nombre es:", nombre, "Tu edad es", edad)

# Conversión de tipos
# int()
# float()
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

x = int(input("Ingresa un número: ")) # El usuario ingresa un 2
print(x * "5") 