from sys import argv

# crear un archivo en mi computadora en la carpeta de downloads

script = argv 

path = "C:/Users/Dell/Downloads"
filename = 'archivo_prueba'
ext = ".txt"

# puedo usar open para crear un archivo si no existe con "w"

print(path + "/" + filename + ext)

newfile = open(path + "/" + filename + ext, "w")
newfile.close()
