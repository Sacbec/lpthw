from sys import argv

nombre_archivo, variable1= argv 
autor = input("Escribe tu nombre: ")
print(f"El nombre del archivo es: {nombre_archivo} y fue creado por {autor}")
print("Esta es la variable que jale con argv: ", variable1)
