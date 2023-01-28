# notas: lo que voy a aprender:
 # 1. como las computadoras modernas guardan los lenguajes humanos al mostrarlos y procesarlos
        # como python 3 llama a estos strings 
#  2. "encode" y "decode" de strings en bytes 
#  3.  manejo de errores 
#  4. COMO LEER CODIGO Y SABER LO QUE HACE INCLUSO SI NUNCA ANTES LO HE VISTO. 

import sys 

# tres variables que se reciben desde la terminal
# uso sys.argv para pasar en orden variables desde la terminal

script, input_encoding, error = sys.argv 

# para definir una funcion necesito
# usar la palabra reservada def
# poner el nombre que tendra la funcion
# abrir parentesis
# colocar los parametros de los que dependera la funcion separados por comas
# cerrar parentesis
# poner dos puntos 

# funcion llamada main que depende de 3 parametros
# se usa uno los parametros para leer por linea con .readline()
def main(language_file, encoding, errors):
    line = language_file.readline() 
    if line: # si line contiene algo, entonces ejecuta la siguiente funcion
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # en este caso la instruccion de devolver, 
    # ejecuta de nuevo la funcion main
    # pienso que se detiene cuando line esta vacia


# funcion llamada print_line que depende de tres parametros 
   
def print_line(line, encoding, errors): 
    next_lang = line.strip() # quita los espacios en blanco del inicio y final 
    raw_bytes = next_lang.encode(encoding, errors = errors ) # encode
    cooked_string = raw_bytes.decode(encoding, errors = errors ) # decode 
    # tanto .encode() como .decode() depende de: encoding y errors

    print(raw_bytes, "<==>", cooked_string) # aqui estoy comparando ambos metodos, .encode(), .decode()

languages = open("languages.txt", encoding = "utf-8")

# llamo a la funcion por su nombre y le paso los parametros de los que depende
main(languages, input_encoding, error) 


# orden de ejecucion:

# 1. he llamado a la funcion main
    # depende de 3 parametros
        # 1. languages: lo defino como un objeto open al archivo txt
        # 2. input_encoding: lo pasare desde la terminal al ejecutar el script
        # 3. error: lo pasare desde la terminal al ejecutar el script

# main toma el archivo .txt, lee una linea y la guarda en la variable: line
# ahora hara preguntas sobre esa variable line:
# si line es true o mejor dicho si line contiene algo, entonces.
# ejecuta a la funcion print_line

# la funcion print_line depende de 3 parametros 
 # 1. line: variable definida en la funcion main (paso anterior)
 # 2. encoding: proviene de input_encoding que se alimenta desde la terminal
 # 3. errors: tambien se alimenta desde la terminal 

 # lo primero que hace es agarrar  la variable line que es la linea que leyo del archivo
 # y le quita los espacios en blanco del inicio y del final, ahora lo guarda en la variable next_lang
 # aplica .encode() a la variable next_lang
 # aplica .decode() a la variable next_lang
 # esta funcion imprime ambos resultados .decode() y .encode()

 # ahora main vuelve a ejecutar a main hasta que line ya no tenga contenido, es decir line = 0
 


