from sys import argv    

script, archivo_nombre = argv

archivo = open(archivo_nombre)


contenido = archivo.read() # estoy probando .readline() solo leer una sola linea

print(contenido)
archivo.close()