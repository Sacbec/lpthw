import sys
# importo sys para poder utilizar sys.argv 
# esto me permite pasarle variables a la terminal y usarlas en mi scrip 

script, input_encoding, error = sys.argv 

# para crear una funcion 
# uso la palabra reservada def 
# despues pongo el nombre que tendra la funcion 
# abro parentesis
# coloco los parametros de los que va a depender la funcion, separados por comas
# cierro parentesis
# pongo dos puntos 
def main(language_file, encoding, errors): # esta funcion depende de un archivo, del encoding, y de los errores
    line = language_file.readline() # ¿lee linea por linea?
    if line: # si line no esta vacía manda a llamar a la siguiente funcion
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # lo que regresa es volver a ejecutar la funcion???

def print_line(line, encoding, errors):
    next_lang = line.strip() # quita los espacios en blanco del inio y del final de la cadena 
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors )

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)

# Pruebas: voy a separar cada linea que hacen las funciones porque aun no entiendo que hacen en conjunto. 

# ¿Qué hace readline()? # no recuerdo si lee linea por linea con cada ejecucion o si lee todo el archivo, o ese es reads()

def pruebas(archivo):
    open_object = open(archivo, "r")
    print(open_object.readline()) # creo que aqui necesito al objeto open para que despues le pueda aplicar
    # read() or readline()
    # Era correcto el pensamiento: para poder leer primero necesito al objeto que open que abre al archivo. 

# pruebas('languages.txt') # no aplica este método porque surge un error de encoding 

# Recordando:
# 1. no existe reads
# 2. read() lee todo el archivo
# 3. readline() lee line por linea 
# pruebas('historia.txt')


# ¿Qué hace .strip() ?

def striping(cadena):
    print(cadena)
    print(cadena.strip())

cadena = "   hola,estoy,bien    "
# striping(cadena)
# lo que hace .strip() es quitar los espacios en blanco del inicio y del final de la cadena