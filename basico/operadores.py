# ----- operadores aritméticos -----
# Un operador es un símbolo del lenguaje de programación, el cual es capaz de realizar operaciones con los valores.
# El enlace de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad, los cuales se encuentran dentro de una misma expresión.
# La mayoría de los operadores de Python tienen un enlazado hacia la izquierda, lo que significa que el cálculo de la expresión es realizado de izquierda a derecha.
'''
Operadores asociados a las operaciones aritméticas
+ -
* / //
%
** 
 -- Lista de prioridades -- 
**
+- los unarios
* / // %
 + - binario
Nota:   sub-expresiones dentro de paréntesis siempre se calculan primero
'''
print(3 + 4)
print(10 - 5) # operador resta, requiere dos argumentos
print(-1) # - signo negativo
print(2*3)
# -- división 
# No intentes:
#   - Dividir entre cero;
#   - Realizar una división entera entre cero;
#   - Encontrar el residuo de una división entre cer
print(6 / 3) # 2.0
print(6 / 3.) # 2.0
print(6. / 3) # 2.0
print(6. / 3.) # 2.0
# -- división entera
# el redondeo siempre va hacia abajo
print(6 // 3) # 2
print(6 // 3.) # 2.0
print(6. // 3) # 2.0
print(6. // 3.) # 2.0
# -- módulo 
# residuo que queda de la división entera 
print(7%2)
# -- potencia
# Cuando ambos ** argumentos son enteros, el resultado es entero, también
# Cuando al menos un ** argumento es flotante, el resultado también es flotante
# el operador de exponenciación utiliza enlazado del lado derecho.
print(2**3)
print(2 ** 2 ** 3) # 256 -> 2 ** 3 = 8 , 2 ** 8 = 256

# ----- operadores de comparación -----
# devuelven True o False
print(3>4)
print(3<4)
print(3>=4)
print(3<=4)

print(3==4)
print(2 == 2.) # true

print(3!=4)

print(3 > 4 == 2)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# ----- operadores lógicos -----
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
