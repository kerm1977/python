print(''' 
El almacenamiento de valores es una forma para poder reutilizarlos luego. Cuando estos valores cambian en el transcurso de una ejecución
del programa, se llama variables. Estos son espacion que se guardan en la memoria del ordenador. Para poder invocar a una variable es
necesario declararla para luego invocarla. Todas las variables deben tener nombres representativos para comprender la función de la misma.

La sintaxis correcta de las variables. Estas deben:
-Las variables contienen un valor por lo que se les asigna con el simbolo igual = 
-Las variables pueden almacenar valores lógicos (True o False)
-Comenzar con numeros
-Contener palabras divididas con _ Ejemplo: variable_Correcta = True (Esa división empezando la segunda palabra en mayúscula se conoce como CAMEL CASE)
-Son caseSensitive (No es lo mismo hola que Hola)
-NO tienen que empezar en mayúscula (Aunque la variable sería reconocida, por convención no debe empezar con mayúsculas)
-NO se pueden usar palabras reservadas por el mismo python
-NO pueden empezar por número
-NO pueden llevar números
-NO usar tíldes ni ñ o signos de puntuación (únicamente _ )

La forma guardar un valor es de la siguiente manera:

>>nombre = valor
>>print(nombre)

''')

variable=6
print("El valor de la variable es: ", variable)


print('''
1. Crea un variable "caramelos "  con valor de 5
2. Crea una variable "Precio "	con valor 2
3. Crea otra variable que calcule el coste de comprar los caramelos
4. Muestra el valor del coste por pantalla
5. Cambia el número de caramelos a 8
6. Cambia el precio a 3
7. Calcula de nuevo el coste
8. Mostrarlo por pantalla
9. Se pueden crear variables múltiples Ejemplo: ............... >>juan, maria = 200, 15
''')

# f-Strings

caramelos= 5
precio = 2
costo= caramelos * precio
print("El costo de los ", caramelos, "caramelos es de: ", costo  )
caramelos = 8
precio = 3
costo= caramelos * precio
print("El costo de los ", caramelos, "caramelos es de: ", costo  )
print("El costo de los  {} caramelos es de: {}" .format(caramelos, costo)) 
print(f"El costo de los  {caramelos} caramelos es de: {costo}") 



print('''
En un juego hay que conseguir 100 puntos entre los dos niveles 
en el nivel 1 tenemos 48 puntos, en el 2 tenemos 62
Calcular los puntos obtenidos en el juego.

Crea una variable cuyo valor sea el resultado de comparar si los puntos totales conseguidos 
son mayor o igual que  los puntos a conseguir

Muestra el valor de la variable por pantalla

''')

puntos_meta=100
nivel_1=48
nivel_2=62
puntos_totales = (nivel_1 + nivel_2)

result = (puntos_totales>=puntos_meta)
print(result)


print(''' 
3 días
convertir 3 días a horas y luego a segundos
''')


horas=24*3
minutos=horas*60

print(f" En 3 días hay {horas} horas que son {minutos} minutos")



print('''
Intercambiar los valores de juan y maría
	''')

juan=200
print(f"El valor de Juan es {juan}")
maria=15
print(f"El valor de María es {maria}")
cambio=juan
juan=maria
maria=cambio

print(f"El intercambio del valor de Juan es {juan} y el valor de maria es {maria}")

print("tambien se puede crear con la variable multiple")
juan, maria=200,15
print(f" El valor de Juan es {juan} el valor de María es {maria}")
juan, maria=maria,juan
print(f"Ahora el valor de Juan es {juan} y el valor de Maria es {maria}")









