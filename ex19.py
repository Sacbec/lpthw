# funcion que se llama cheese_and_crackers
# recibe dos parametros
def cheese_and_crackers(cheese_count, boxes_of_cranckers):
    # imprime cuantos quesos tengo
    # mediante format usa el valor del parametro que se le paso
    print(f"You have {cheese_count} cheeses!")
    # imprime cuantos crackers tengo
    print(f"You have {boxes_of_cranckers} boxes of crancerks !")
    # mediante format usa el valor del parametro que se le paso
    
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

# nota: como la funcion solo imprime los parametros que recibe, pueden ser numericos o de tipo string

print("We can just give the function numbers directly:")
# Para llamar / ejecutar una funcion necesito usar su nombre, 
# parentesis y dentro indicar los parametros
# en este caso use enteros como parametros
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# para ejecutar / llamar a una funcion necesito escribir su
# nombre, y dentro de los parentesis indicarle los parametros que
# va a recibir
# En este caso le pase variables como argumentos, éstas a su vez
# almacenan numeros enteros

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# para llamar /ejecutar una funcion solo debo escribir su nombre y
# dentro de los parentesis indicar los parametros que va a usar
# en este caso esta usando operaciones matematicas en el lugar
# de cada parametro
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
# para llamar a una funcion solo debo escribir su nombre
# y dentro de sus parentesis indicar los valores que va a 
# recibir como parametros 
# en este caso se hacen operaciones matematicas con las variables
# creadas anteriormente
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# una funcion puede recibir, integers, floats, strings, vairables -> realmente pude recibir de todo
# mientras que este permitido realizar las operaciones con esos datos.