from sys import argv 

script, input_file = argv # a través de la libreria argv 
# puedo recibir variables desde la terminal 
# por ejemplo, aqui voy a recibir el nombre del script  y el nombre del archivo que usare en mi codigo. 
def print_all(f): # para crear una funcion necesito invocar def seguido del nombre de la funcion
    #de parentesis, de los argumentos que usara la funcion, cierro parentses y uso dos puntos. 
    """ 
    Funcion que recibe un parametro. 
    Usa ese parametro para aplicarle el metodo .read()
    Para poder aplicar el metodo .read() el parametro debe contener un objeto open. 
    """
    print(f.read()) # lee al objeto open

def rewind(f): # para crear una funcion necesito invocar def seguido del nombre de la funcion, abro
    # parentesis, coloco los parametros que usara la funcion, cierro parentesis y pongo dos puntos. 
    """ Esta funcion reibe un parametro
    y coloca el cursos en la posicion 0 del contenido. 
    """
    f.seek(0) # coloca el cursor en la posicion 0 del contenido. 
    # para que yo pueda usar .seek(0), el parametro que le estoy pasando a la funcion debe ser
    # un objeto open

def print_a_line(line_count, f): # para crear una funcion necesito invocar def seguido del nombre
    # de la funcion, abro parentesis, pongo los parametros de los que dependera la funcion cierro 
    # parentesis y pongo dos puntos
    print(line_count, f.readline()) # imprime el conteo de la linea y lee una linea del objeto open
    # para poder usar .readline() el parametro f, que le pase a la funcion, debe ser un objeto open

current_file = open(input_file) # variable que almacena al objeto open

print("First let's print the whole file:\n")
# ¿cual de todas mis funciones lee todo el contenido del objeto open?
# .read()

print_all(current_file) # para llamar a una funcion necesito su nombre, abrir parentesis, colocar
# el o los parametros de los que depende, y cerrar parentesis. 