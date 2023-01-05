def chokies_y_mantecadas(galletas, pancito):
    print(f"Un paquete nuevo de chokies tiene {galletas} galletas.")
    print(f"Un paquete nuevo de mantecadas tiene {pancito} pancitos.")
    print("Eso es mucho pan y mucha azucar.")
    print("Despues de comer eso deberia ir al gimnasio. \n")

# 10 formas diferentes de llamar a mi funcion

# forma 1: ambos integer
chokies_y_mantecadas(10, 6)
# forma 2: un integer y un float
chokies_y_mantecadas(10, 3.5)
# forma 3: usando variables
total_mantecadas = 6
total_galletas = 6
chokies_y_mantecadas(total_galletas, total_mantecadas)

# forma 4: una variable y un integer

chokies_y_mantecadas(total_galletas, 6)

# forma 5: dos float

chokies_y_mantecadas(3.5, 2.5)

# forma 6: operaciones matematicas en ambos parametros entre variables y enteros
chokies_y_mantecadas(total_galletas-1, total_mantecadas-1)

# forma 7: operaciones matematicas en ambos parametros entre variables y flotantes

chokies_y_mantecadas(total_galletas - 2.5 , total_mantecadas - 5)

# forma 8 : 