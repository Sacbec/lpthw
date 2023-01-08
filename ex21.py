def add(a, b): # para crear una funcion uso la palabra reservada def, luego el nombre
    # de la funcion, abro parentesis, coloco los paramentros de los que va a depender
    # cierro parentesis y pongo dos puntos
    print(f"ADDING {a} + {b} ") # va a imprimir que esta sumando y con format mostrara los valores
    # que entraron como parametros
    return a + b # uso return para almacenar la suma de a + b

def subtract(a, b): # para crear una funcion uso la palabra reservada def
    # despues pongo el nombre que tendra la funcion, abro parentesis, coloco los 
    # parametros de los que va a depender, cierro parentesis y pongo dos puntos. 
    print(f"SUBTRACTING {a} - {b}")
    return a - b # uso return para almacenar la suma de a - b

def multiply(a, b): # para rear una funcion uso la palabra reservada def, 
    # luego va el nombre que tendra la funcion
    # abro parentesis
    # despues los parametros de los que va a depender, separados por comas
    # cierro parentesis
    # pongo dos puntos
    print(f"MULTIPLYING {a} * {b}")
    return a * b # uso return para almacenar la multiplicacion entre a y b 

def divide(a, b): # para crear una funcion necesito usar la palabra reservada def
    # luego el nombre que tendra la funcion
    # abro parentesis
    # pongo los parametros de los que va a depender la funcion
    # cierro parentesis
    # pongo dos puntos 
    print(f"DIVIDING {a} / {b}")
    return a / b # uso return para almacenar el valor de a / b

print("Let's do some math with just functions!")

age = add(30, 5) 
# primero mando a llamar a la funcion escribiendo su nombre, 
# abro parentesis
# le paso los parametros de los que depende
# cierro parentesis
# ahora estoy guardando el valor que resulta de llamar a la funcion con
# los valores 30 y 5 
height = subtract(78, 4) 
# primero mando a llamar a la funcion escribiendo su nombre
# abro parentesis
# le paso los parametros de los que depende
# cierro parentesis
# luego guardo el resultado que regresa la funcion en otra variable
weight = multiply(90, 2) 
# primero mando a llamar a la funcion escribiendo su nombre
# abro parentesis
# le paso los paramentros de los que depende
# cierro parentesis
# ahora guardo el valor que regresa la funcion en otra variable 
iq = divide(100, 2)
# primero mando a llamar a la funcion escribiendo su nombre
# despues abro parentesis
# le paso los parametros de los que depende
# cierro parentesis
# ahora guardo el resultado que me regresa la funcion en otra variable 

# guardo el resultado que generan las funciones en otras variables para tener la libertad
# de usarlas en algun otro momento

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway. 

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# puedo llamar a una funcion escribiendo su nombre
# abrir parentesis
# pasarle los parametros de los que depende
# en este caso los parametros que le estoy mandando tambien son funciones
# es decir que primero se necesitan ejecutar las funciones interiores
# una vez que arrojen su resultado, ese se tomara como parametro para la funcion exterior
# cierro parentesis
# almaceno el resultado de las constantes evaluaciones en una variable

print("That becomes: ", what, "can you do it by hand?")

# haciendolo a mano: divide -> 25, weight -> 180 : 4,500
# 74 -4500: -4426
# -4391- > fue correcto. 

# nota: 
# solo las funciones que invoco explicitamente y dentro tienen un print, son las que 
# muestran ese mensaje
# pero por ejemplo si estoy usando, como paso intermedio, a otra funcion que tambien imprime
# pero yo no la invoque directamente (escribi su nombre para invocarla) entonces no
# imprime su mensaje aunque contenga un print dentro de ella. 