""":
-Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
-Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
-(Ten en cuenta que cada lenguaje puede poseer unos diferentes)
-Utilizando las operaciones con operadores que tú quieras, crea ejemplos
-que representen todos los tipos de estructuras de control que existan
-en tu lenguaje:
-Condicionales, iterativas, excepciones...
-Debes hacer print por consola del resultado de todos los ejemplos.

######################################################################################################

-DIFICULTAD EXTRA (opcional):
-Crea un programa que imprima por consola todos los números comprendidos
-entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
-Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Operadores aritmeticos

"""
Suma (+): Suma dos números
Resta (-): Resta el segundo número del primero 
Multilicación (*): Multiplica dos números

(39 dividido entre 5)

Dividendo: El número que se va a dividir es 39. En este caso, 37 es el dividendo.
Divisor: El número por el cual se divide es 5. En este caso, 5 es el divisor.
Cociente: El resultado de la división es 7. El cociente es la parte entera del resultado.
Resto: El residuo o resto de la división es 4. Esto significa que no podemos dividir 39 exactamente entre 5; sobran 4 unidades.

División (/): Devuelve el cociente (resultado) con todo y decimales 
División entera(//): Devuelve el cociente sin el residuo (sin los decimales)
Módulo (%): devuelve el resto de la división(La cantidad de unidades que faltan para llegar al dividendo)

Potencia(**): Eleva un número a la potencia del otro.

"""

# Ejemplos 

a = 39
b = 5 

suma  = a+ b
resta = a-b
resta_negativa =b-a
multiplicacion = a*b
division = a / b 
division_entera= a//b
modulo = a%b
potencia = a ** b


print ("Suma", suma)
print ("Resta", resta)
print ("Resta negativa", resta_negativa)
print ("Multiplicación", multiplicacion)
print ("División", division)
print ("División entera", division_entera)
print ("Módulo", modulo)
print ("Potencia", potencia)

"""Operadores de compración

Igual: ==
Diferente: !=
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=

"""

# Comparaciones  
x = 10  
y = 20  
print("x es igual a y:", x == y)  
print("x es diferente de y:", x != y)  
print("x es mayor que y:", x > y)  
print("x es menor que y:", x < y)  
print("x es mayor o igual que y:", x >= y)  
print("x es menor o igual que y:", x <= y)

""" Operadores lógicos

Y: and
O: or
Negación: not

"""
# Operadores Lógicos  
a = True  
b = False  
print("a y b:", a and b)  
print("a o b:", a or b)  
print("Negación de a:", not a)






