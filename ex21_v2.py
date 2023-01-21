# para crear una funcion necesito usar la palabra reservada def
# luego pondo el nombre que tendra la funcion 
# abro parentesis
# le paso los parametros de los que va a depender la funcion, separados por comas
# cierro parentesis
# pongo dos puntos 
def add(numero1, numero2):
    print(f"Estoy haciendo la suma de {numero1} y {numero2}")
    return numero1 + numero2 
# notar que no imprimo nada con el return, unicamente uso return para almacenar el resultado de la operacion, en este caso de una suma

# para crear una funcion uso la pabra reservada def
# despues escribo el nombre que tendra la funcion 
# abro parentesis
# le paso los parametros de los que dependera la funcion, separados por comas
# cierro parentesis
# escribo dos puntos

def  subtract(numero1, numero2):
    print(f"Estoy haciendo la resta de {numero1} - {numero2} ") 
    return numero1 - numero2 

# para crear una funcion uso la palabra reservada def
# ahora escribo el nombre que tendra la funcion 
# abro parentesis 
# escribo los parametros, separados por comas, de los que dependera la funcion 
# cierro parentesis
# pongo dos puntos

def multiply(factor1, factor2):
    print(f"Estoy haciendo la multiplicacion entre {factor1} y {factor2}")
    return factor1 * factor2 

# para crear una funcion uso la palabra reservada def
# ahora escribo el nombre que tendra la funcion 
# abro parentesis
# coloco los parametros de los que dependera la funcion, tienen que ir separados por comas 
# cierro parentesis
# escribo dos puntos 

def divide(primervalor, segundovalor):
    print(f"Estoy haciendo la division entre {primervalor} y {segundovalor}")
    return primervalor / segundovalor 

print("Let's do some math with just functions!")

# para ejecutar una funcion
# escribo su nombre
# abro parentesis
# le paso los paramentros de los que depende, separados por comas
# cierro parentesis

age = add(2, 3) # el valor que regresa la funcion es almacenado en return y a su vez es guardado en esta otra variable 
# aunque no imprimo el valor resultado de la funcion, puedo usarlo en el lugar que yo quiera con la variable que almacena el resultado

# para ejecutar una funcion necesito 
# escribir su nombre
# abrir parentesis 
# pasarle los argumentos, separados por comas, de los que depende
# cerrar parentesis 

height = subtract(10, 5) # return almacena el resultado de la operacion de la funcion
# el resultado de result es guardado en esta variable 
# como llame a la funcion y ella dentro de si tiene un print, tambien imprimira su mensaje

# para ejecutar una funcion necesito 
# escribir su nombre 
# abrir parentesis
# pasarle los argumentos, separados por comas, de los que depende

weight = multiply(3, 5)  # return almacena el resultado de la funcion
# como la funcion tiene un print se imprimira

# para ejecutar una variable necesito
# escribir su nombre 
# abrir parentesis
# pasarle los argumentos, separados por comas, de los que depende
# cerrar parentesis

iq = divide(180, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Estoy imprimiendo las variables que guardan el valor que contiene return de cada una de las funciones usadas. 
# esa es la razon de que no vuelve a imprimir el valor que contiene la funcion, porqu no la estoy llamando, 
# unicamente estoy llamando a la variable que ya almacena el valor de la funcion a través del return 

# A puzzle for extra credit, type it in anyway
print("Here is a puzzle.")
# para ejecutar una funcion necesito 
# escribir su nombre
# abrir parentesis
# pasarle los parametros, separados por comas, de los que depende
# cerrar parentesis 

what = add(age, subtract(height, multiply(weight, divide(iq, 2 )  ) ) )

# Si tengo una funcion cuyos parametros son otras funciones
# por esa razon necesito evaluar primero las funciones de adentro
# primero ejecutare la funcion que este mas adentro de la cadena 
# en este caso divide() es la funcion centro, primero la ejecuto y de ahi voy hacia afuera
# por eso al ejecutar el script, primero se imprime el contenido de la funcion divide()

print("That becomes: ", what, "Can you do it by hand?")


# desglosando el encadenamiento de funciones

print( (2+3) + (( 10-5 ) - ((3*5) * ((180/2) / 2)) ) )
print(" a manita: ",   (9+23) + (( 9283-9283 ) - ((54*923928) * ((9238/54) / 14)) )     )

what2 = add(add(9, 23), subtract(subtract(9283, 9283), multiply(multiply(54, 923928), divide(divide(9238, 54), 14)) ))
print(f"The result of what2 is: {what2}")

# como el objetivo de la funcion es ejecutar el mismo proceso sin volver a escribirlo
# lo estoy usando en diferentes partes de la formula
# si necesito 