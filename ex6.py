types_of_people = 10 # declaro una variable 
x = f"There are {types_of_people} types of people." # con f de format al inicio del string puedo
# insertar variables definidas anteriormente

binary = "binary" # defino una variable con un string
do_not = "don't" # defino otra variable con un string
y = f"Those who know {binary} and those who {do_not}." # al pasar f de format puedo meter todas las 
# variables que yo quiera a mi string

print(x) # imprimir la variable x que ademas esta jalando con f de format variables definidas 
#previamente
print(y) # imprimir la variable y que ademas esta jalando con f de format variables definidas 
#previamente

print(f"I said: {x}") # con f de format estoy jalando la variable x, que a su vez esta jalando otra variable
print(f"I also said: '{y}'") #con f de format estoy jaland la variable y, que a su vez esta jalando 
# otra variable 

hilarious = False # defino una variable con un booleano
joke_evaluation = "Isn't that joke so funny?! {}" # defino una variable con un string que contiene {}
# puedo insertar variable en strings que contienen {}


print(joke_evaluation.format(hilarious)) # FORMAT SE USA PARA STRINGS YA CREADAS

w = "This is the left side of..." #creo una variable con un string
e = "a string with a right side." # creo una variable con un string

print(w + e) # a través de print puedo sumar o concatenar cadenas o strings