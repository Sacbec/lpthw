from sys import argv # libreria que me permite pasar variaables en la terminal
from os.path import exists # libreria que me permite confirmar si existe un archivo

script, from_file, to_file = argv # nombre del script a correr, nombre del archivo a copiar
# nombre del archivo en donde se depositara

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?
in_file = open(from_file) # creo el objeto open 
# archivo desde el que se va a extraer
indata = in_file.read() # leo el objeto open
# imprimo en pantalla el contenido del archivo fuente

print(f"The input file is {len(indata)} bytes long") # longitud del archivo

print(f"Does the output file exist? {exists(to_file)}") # comprueba si existe? ¿en donde revisa?
# True si existe, False si no existe
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input() # pausa para decidir si continuar o cancelar 

out_file = open(to_file, 'w') # crear el objeto open con modo "w" write para escribir 
# contenido en el archivo
# archivo en el que se va a depositar contenido

out_file.write(indata) # escribir en out_file lo que contiene indata
# escribo en el archivo que abri con el modo "w"

print("Alright, all done.")

out_file.close() # cierro out_file
in_file.close()  # cierro in_file