# write a script that uses read and argv to read the file you just created
from sys import argv 

script, filename = argv # nombre del script y nombre del archivo a leer

file = open(filename) # crear objeto open 
content = file.read()

print(content)

print("Archivo cerrado.")