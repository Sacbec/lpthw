# para crear una funcion uso la palabra reservada def
# despues escribo el nombre  que tendra la funcion 
# abro parentesis
# si la funcion va a usar aparametros los pongo dentro de los parentessis, deben ir separados por comas
# cerrar el parentesis 
# poner dos puntos
space = ' '

def f1():
    return "f1" 

def f2(arg):
    return arg + space + "f2"

def f3(arg):
    return arg + space +  "f3"

# para llamar a una funcion necesito:
# escribir su nombre 
# abrir parentesis
# pasarle los argumentos de los que depende
# cerrar parentesis 

f3( f2( f1())) # este es un encadenamiento de funciones, primero se va a ejecutar f1 porque es la funcion centro y de ahi dependen las demas
# el resultado que arroje f1 servira de parametro para f2 y
# despues con el resultado de f2 podre alimentar a f3

# print(f3(f2(f1()))) uso este comando para imprimir el resultado 

def chain(start, *funcs ):
    res = start # asigno el parametro star a una nueva variable 
    for func in funcs: # extraigo cada elemento del parametro funcs:
        res = func(res) # ahora ejecuto la funcion que viene en la lista funcs y la alimento con res, que esta guardando el parametro
        # con el que tambien alimente a la funcion 
        return res # ahora devuelvo el nuevo valor de res, que esta guardando el resultado de ejecutar cada funcion con el antiguo valor de res

# entonces chain depende de dos parametros, el primero sera el ingrediente de cada una de las siguientes funciones a ejecutar
# funcs parece ser una lista de funciones

def increment(arg_test):
    return arg_test +1 

inc_1 = chain(0, increment, increment, increment ) # Nota: ESTOY LLAMANDA A UNA FUNCION SIN ABRIR PARENTESIS. !!!
# la unica manera de llamar a una funcion sin parentesis es cuando funciona como parametro para alimentar a otra funcion. 
print("esto es inc_1: ", inc_1)