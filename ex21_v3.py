# crear funcion max
def maximo(numero1, numero2):
    if numero1 > numero2 :
        maximo = numero1
    else:
        maximo = numero2
    return maximo 

print(f"El numero maximo es: {maximo(3, 40)}")

# max de 3 numeros

def maximo_tres(numero1, numero2, numero3) :
    if numero1 > numero2 :
        maximo = numero1
    elif numero2 > numero3:
        maximo  = numero2 
    else:
        maximo = numero3 
    return maximo 

print(f"El maximo de los tres numeros es: {maximo_tres(10, 200, 3) }")

