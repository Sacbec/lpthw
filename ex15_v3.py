from sys import argv

script, filename = argv #argv almacenara la variable script y la variable filename

# para leer necesito el comando open() y dentro el nombre del archivo
# ese contenido se debe almacenar en una variable

txt = open(filename) # necesito la instruccion open(nombre del archivo)
    # observar que no estoy harcodeando el nombre del archivo, lo estoy pasando como una variable


print(f"Here's your filename {filename}")
print(txt.read()) # le estoy mandando la instruccion read a la variable que guardo el contenido que abri del archivo que le pase


print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())