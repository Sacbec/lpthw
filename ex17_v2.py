from sys import argv 
from os.path import exists

script, source_name, target_name = argv 

# comprobar que existe el archivo fuente
print("Comparando si existe el archivo fuente: ")
print("Existe?", exists(source_name))

print("Abriendo el archivo fuente: ")

source = open(source_name, 'r').read() # creo un objeto open en modo read para abrir el archivo source
# leo el contenido
target = open(target_name, 'w') # creo un objeto open en modo write para escribir el contenido del archivo source

print(f"Escribiendo el contenido de la fuente {source_name} dentro de {target_name}.")
target.write(source) # en este paso ya escribi el contenido de la fuente en el destino


print(f"Cerrando los archivos {source_name} y {target_name}. ")
target.close()
source.close()