print(''' 

OPERADORES DE COMPARACION
Devuelve valores booleanos.

-Igual que ==
-Distinto que !=
-menor que <
-menor igual que <=
-Mayor que >
-Mayor igual que >=
-Asignación =


Ejemplo:
15 > 3 -> True
5 < 1  -> False
3 == 3 -> True  
4 == 2+2 -> True


PRESCENDENCIA DE OPERADORES
Siempre se va a ejecutar lo operadores aritméticos y
luego se ejecutan lo de comparación

Ejemplo:

8 + 0 > 8 -> False
10 != 5 * 2 -> False

''')

print("El resultado de:  4+3 > 6-1 es:", 4+3 > 6-1)
print("El resultado de:  6+2*3 == 9/3*4 es: ", 6+2*3 == 9/3*4)
print ("En la operación anterior primero multiplica 2*3==6 +6 son 12,  luego divide 9/3==3 * 4, son 12 y luego compara los resultados. True")





