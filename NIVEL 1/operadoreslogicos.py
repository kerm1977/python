print(''' 

OPERADORES DE COMPARACION
Devuelve valores booleanos.

-and -> Tienen que cumplirse ambas operaciones.
-or -> Se puede complir una de las dos operacion. Or es inclusivo por lo tanto si las ambas expresiones son verdaderas igual da true
-not -> Si es falso not lo convierte en verdadero. Ejemplo not 2>1-- aunque la expresión es verdadera, not la pasa a falso



''')

print("El resultado de 2+2==4 and 5>3:", 2+2==4 and 5>3, "Porque ambas operaciones se cumplen.")

print("El resultado de True + True es: ", True + True, "porque las 2 condiciones se cumplen por lo tanto dos verdaderos, suma." )
print("El resultado de True + False es: ", True + False, "porque una de la condicion se cumple por lo tanto suma la cantidad de verdaderos. ")
print("El resultado de False + False es: ", False + False, "porque ninguna condición se cumple por lo tanto no suma proque todo es falso." )

print("------AND-------------------")
print("El resultado de True and True es: ", True and True, "")
print("El resultado de True and False es: ", True and False, "")
print("El resultado de False and False es: ", False and False, "")
print("------OR--------------------")
print("El resultado de True or True es: ", True or True, "")
print("El resultado de True or False es: ", True or False, "")
print("El resultado de False or False es: ", False or False, "")


