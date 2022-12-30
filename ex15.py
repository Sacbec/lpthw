from sys import argv

script, filename = argv # nombre del script,
# nombre del archivo a leer

txt = open(filename) # variable que guarda el resultado de open

print(f"Here's your file {filename}:") # imprime el nombre del
# archivo
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
