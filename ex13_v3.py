from sys import argv 

nombre_archivo, fecha, autor = argv
# puedo pasar variables en la terminal que tienen espacios usando double quotes
# argv es una forma de input que recibe las variables desde la terminal
# input recibe las variables desde el script, siento que es una forma mas flexible
print("Hare una suma")
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro numero: "))
print(f"""La suma de ambos numeros es: {numero1 + numero2}, estan en el archivo {nombre_archivo} y fue creado en la fecha {fecha} por el autor {autor}.""")