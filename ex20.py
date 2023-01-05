from sys import argv 

script, input_file = argv 

def print_all(f): # funcion que recibe un solo parametro
    print(f.read())

def rewind(f): # funcion que recibe un solo parametro
    f.seek(0) # es un cursor ?

def print_a_line(line_count, f): # funcion que recibe dos parametros
    print(line_count, f.readline()) # imprime line_count y una linea
    # si imprimo varias veces .readline() lee la siguiente linea?

current_file = open(input_file) # le tengo que pasar un input_file desde la terminal

print("first let's print the whole file: \n")

print_all(current_file)

# la funcion recibe un parametro llamado f, 
# mas tarde defino una variable que almacena el objeto open que abre un archivo
# cuando llamo a la funcion por su nombre, no necesito pasar a f, f solo representa que esa 
# funcion admite un parametro, lo que realmente le voy a pasar es
# la variable current_file que esta almacenando el objeto open

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# es decir que el resultado de imprimir por lineas cambia si no hago el 
# rewind ???
# exacto, si no hago rewind(0) el puntero se va al final y .readline()
# imprime lineas vacias. 