# para crear una funcion debo usar la palabra reservada def
# despues pongo el nombre que tendra la funcion 
# abro parentesis
# pongo los parametros de los que depende la funcion 
# cierro parentesis
# pongo dos puntos 
import sys

script, input_encoding, error = sys.argv 

def main(language_file, encoding, errors):
    line = language_file.readline() 
    if line: 
        print_line(line, encoding, errors) # llama a una funcion que aun no defino
        return main(language_file, encoding, errors) # regresa el llamado de una funcion
    

def print_line(line, encoding, errors):
    next_lang = line.strip() # usa el parametro que le pase para quitarle los espacios en blanco 
                            # del inicio y del final
    raw_bytes = next_lang.encode(encoding, errors = errors) # le aplica encode 
    cooked_string = raw_bytes.decode(encoding, errors = errors ) # lo que esta encode ahora lo decode


    print("raw: ", next_lang, "encode: ", raw_bytes, "<==>","decode: ",  cooked_string) # 

languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)