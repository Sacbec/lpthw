from sys import argv

script, filename = argv # nombre del script,
                        # nombre del archivo a leer

txt = open(filename) # variable que guarda el resultado de open
# en este punto estoy creando un objeto open. 
txt.close()
print(f"Here's your file {filename}:") # imprime el nombre del
# archivo
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) # guardo el contenido de open

print(txt_again.read()) # .read() sobre la variable que trae el contenido de open 

txt_again.close()