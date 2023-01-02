# this one is like yout scripts with argv 
def print_two(*args): # lo interesante aqui es que le puedo pasar todos los paramentros que 
    # yo quiera!!!!
    arg1, arg2 = args 
    print(f"arg1: {arg1}, arg2_ {arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # funcion que se llama print_two_again() y recibe dos argumentos
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument 
def print_one(arg1): # funcion que se llama print_one y recibe un solo parametro
    print(f"arg1 {arg1}") # imprime el nombre de la variable y su valor

#this one takes no arguments
def print_none(): # funcion que se llama print_none y no recibe argumentos
    print("I got nothin'.")

print_two("Zed", "Shaw") # llamo a la funcion print_two, le paso dos parametros
# ¿que pasa si le doy mas? # pienso que no importa porque solo tomara los primeros dos y los 
# asiganara a variables 
print_two_again("Zed", "Shaw") # llamo a la funcion print_two_again y le paso dos parametros
print_one("First!") # llamo a la funcion print_one, solo recibe un parametro, observar que 
# todos los parametros los he pasado como strings-> porque son strings. 
print_none() # llamo a la funcion, le pongo sus parentesis aunque no reciba argumentos. 