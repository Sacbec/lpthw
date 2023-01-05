from sys import argv 

script, input_file = argv 

def print_all(f): # funcion que depende del parametro f
    print(f.read())

def rewind(f): # funcion que depende del parametro f
    f.seek(0) # al cursor del parametro lo regresa a la posicion 0

def print_a_line(line_count, f): # funcion que depende de dos parametros
    print(line_count, f.readline())

current_file = open(input_file) # variable que almacena el objeto open

print("First let's print the whole file:\n")

print_all(current_file) # llamo a la funcion, parentesis, parametro
# en este caso el parametro es la variable que esta almaenando al 
# objeto open
print("Now let's rewind, kind of like a tape.")

rewind(current_file) # llamo a la funcion por su nombre, parentesis y
# dentro el parametro, que en este caso es la variable que 
# guarda al objeto open 
# lo que hara esta funcion es regresar el cursor a la posicion 0

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) 
# la funcion print_a_line depende de dos parametros, uno lo imprime tal
# cual llega y al otro le aplica .readline(), en este caso le estoy pasando
# current line que vale 1, y current_file que esta guardando al objeto open
# por lo una vez que lo tome la funcion, entonces tambien le estaria 
# aplicando .readline()
current_line = current_line + 1
print_a_line(current_line, current_file) # para ejecutar la funcion
# la llamo por su nombre, le pongo parentesis y le paso los parametros
# en este caso depende de dos, de line_count y de f
# yo le pasaré current_line para line_count y current_file para f
# para este punto current_line ya aumento en 1
# mientras que current_file es la variable que almacena al objeto open

current_line = current_line + 1
print_a_line(current_line, current_file)
