# ----- Hola mundo -----
#  esto es un comentario de una sola linea
"""
Esto es un comentario 
en varias
lineas
"""
'''
Esto también es un comentario
en varias 
lineas
'''
print("¡Hola, Mundo!")
# print(Hola) Error -> Hola is not defined
# print "hola" Error -> Missing parentheses in call to print
print("Hola Python")
# ----- Caracteres de escape -----
# \n linea nueva 
print("La Witsi Witsi Araña \n subió a su telaraña.")
# \ barra invertida 
print("\\")

# ----- Argumentos posicionales -----
# el significado de estos argumentos se toma no de su ubicación
print("Mi nombre es", "Python.")
# primero se imprimirá Mi nombre es y luego Python

# ----- Argumentos de palabra clave -----
# El nombre proviene del hecho de que el significado de estos argumentos se toma de la palabra especial (palabra clave) utilizada para identificarlos.
print("Mi nombre es", "Python.", end="****")
print("Monty Python.")
# el valor por defecto de end es \n
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")
# print(sep="&", "fish", "chips") Error -> positional argument follows keyword argument



# ----- tipos de datos - Literales  -----
# Un literal se refiere a datos cuyos valores están determinados por el literal mismo.
# por ejemplo el numero 123
# c no es un literal, puede representar muchos valores
# Se utilizan literales para codificar datos y ponerlos dentro del código.
# cadenas de texto
print("Cadena de texto con comillas dobles")
print('Cadena de texto con comillas simples')

print("Operador type ->", type("Hola Python"))

# --- Números ---
# enteros
print(5)
print("Operador type ->", type(5))
# punto flotantes
print(1.5)
print("Operador type ->", type(1.5))
# octal
print(0o123)
print("Operador type ->", type(0o123))
# hexadecimal 
print(0x123)
# notación exponencial
print(3E8)
print(6.62607E-34)
print("Operador type ->", type(0x123))
print(1+2j)
print("Operador type ->", type(1+2j))



# --- Booleanos ---
print("Operador type 'True' ->", type(True))
print("Operador type 'False'->", type(False))
print(True > False)
print(True < False) 