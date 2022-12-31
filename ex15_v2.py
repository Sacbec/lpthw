from sys import argv    

script, archivo_nombre = argv

archivo = open(archivo_nombre)

contenido = archivo.readline() # estoy probando .readline() solo leer una sola linea

print(contenido)