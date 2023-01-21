def concatenador(palabra1, palabra2):
    print(f"Estoy concatenando {palabra1} con {palabra2}")
    return palabra1 + ' ' + palabra2

resultado_conca = concatenador('pan', 'queso')

# estoy haciendo esto porque quiero probar que return puede almacenar cualquier cosa

print(f"Un return puede almacenar strings como: {resultado_conca} ")

# el return esta almacenando una suma de cadenas y tambien de espacios en blanco


# ahora intentare que regrese variables

def func_variables(variable1, variable2):
    print(f"Hare operaciones con {variable1} y {variable2} e intentare almacenar variables en return ")
    x = 5
    y = 10
    return x*variable1 + y*variable2  # incluso puedo hacer operaciones con parametros y variables  dentro de return 

resultado_var = func_variables(3, 4)
print(resultado_var)

# quiero una funcion que me salude cada que inicie 

def saludar_usuario():
    usuario_nombre = input("Este es el inicio del programa. ¿Cuál es tu nombre? : ")
    print(f"Bienvenido {usuario_nombre} !!!")
    print("Podremos hacer muchas cosas con funciones en este script :D ")

saludar_usuario()

# ejercicio: funcion que recibe dos parametros pero uno ya tiene un valor asignado 

def valor_asignado(valor1 , valor2 = 3): # no es posible asignar el parametro a un valor antes de un parametro que sera ingresado
    print(f"Estoy recibiendo dos parametros {valor1} y {valor2}")

valor_asignado(10)

# prueba de pasar parametros por default, pero ver si jala los que yo le doy si se los paso

def default(automa1 = 1, automa2 = 2):
    print(f"Estoy imprimiendo {automa1} y {automa2} ")
 # le dio preferencia a los valores que yo le meti, sobre los que ya tenia asignados
default(4,3)
default()


# usare una funcion para revisar valores
# tengo una lista de mediciones de alcohol a conductores [23, 98, 34, 36, 23, 45 ,56, 12, 34, 45, 56, 67, 78, 89, 28]
# si pasa lso 20 entonces sera alcoholico
medidas = [23, 98, 34, 36, 23, 45 ,56, 12, 34, 45, 56, 67, 78, 89, 28]
def medir_alcohol(medicion_alcohol, limite = 20 ):
    if medicion_alcohol > limite :
        return "Persona alcoholizada" # return puede almacenar cualquier tipo de valor 
    else:
        return "Dentro del rango" # return puede almacenar cualquier tipo de valor 
limite = 50   
for medicion in medidas:
    resultado = medir_alcohol(medicion, limite)
    print(resultado)

# el objetivo de una funcion es repatir el proceso sin volver a escribirlo
# en este caso estoy usando una sola funcion para comprobar sobre todos los valores
# comparado contra escribir codigo para evaluar cada valor, porque en este caso tendria que escribir el mismo codigo que evalua 15 veces
# porque hay 15 valores. 