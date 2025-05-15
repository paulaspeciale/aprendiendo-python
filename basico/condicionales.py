# ----- Condicionales -----
mi_condicion = True
if mi_condicion:
    print("Se ejecuta la condición del if")
print("La ejecución continúa")

mi_condicion_expr = 2 * 3
if mi_condicion_expr:
    print("Se imprimirá esto?")
if mi_condicion_expr == 6:
    print("2*3")
if mi_condicion_expr > 3:
    print("2*3 > 3")
else :
    print("2*3 < 3")

var = 5
if var > 2:
    print (var," > 2")
elif var == 2:
   print (var," = 2")
else:
    print (var," < 2")

if "":
    print("una string vació es True ?")
else:
    print("una string vacía es False")

if var >= 5 or var < 3:
    print(var,"> 5 or", var," < 3")