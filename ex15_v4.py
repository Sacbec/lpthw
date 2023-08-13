from sys import argv 

script, filename = argv # recibe parametros del usuario, el primero es el nombre del archivo

txt = open(filename) # abre el archivo y guarda el contenido en una variable

print(f"Here's your file {filename}") # imprime el nombre del archivo
print(txt.read()) # método read a la variable que almacena el contenido que viene de open()

print("Type the filename again: ")
file_again = input("> ") # al inicio pase el nombre del archivo desde powershell,
# ahora quiero que el usuario lo escriba

txt_again = open(file_again)

print(txt_again.readline())