from sys import argv 

script, filename = argv 

print("python esta abriendo el archivo con: open(filename, 'w') ")
space = "\n" 

print(space)

file = open(filename, "w") # modo "w" permite escribir dentro del archivo pero primero hace truncate

print("A continuacion hay que ingresar las lineas que se escribiran en el archivo")
line1 = input("ingresa la linea 1: ")
line2 = input("ingresa la segunda inea: ")
line3 = input("ingresa la tercera linea: ")
print(space)



file.write(line1)
file.write(space)
file.write(line2)
file.write(space)
file.write(line3)
file.write(space)



print("Python esta cerrando el archivo con .close()")
print(space)
file.close()

print("Ahora me gustaria ver el achivo.")
print("Python abrira el archivo con open(filename), el modo por default es 'r'")

file = open(filename, "r")
print("El contenido que acabo de agregar al archivo es: ")
print(space)

print(file.read())
print("Python esta cerrando el archivo con .close()")
file.close()