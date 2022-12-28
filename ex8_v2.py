formatter = "{} {} {} {}"

print( formatter.format(1,2,3,4) )
print( formatter.format('one', 'two', 'three', 'four'))
print( formatter.format(True, False, False, True))
print( formatter.format(formatter, formatter, formatter, formatter))
# {} es el comando clave para meter valores con .format()
# ¿que ocurre si no le meto todas las variables?
print( formatter.format('solo una ', 'ahora dos', 'tres', 'y 4'))
print(formatter.format(
    "Try your", 
    "Own text here", 
    "Maybe a poem", 
    "Or a song about fear"
))


# que pasa si le quito una llave a la cadena 

formatter2 = " cadena {} {} {}"

print(formatter2.format(1, 2, 3, 4)) # no arroja error si le paso mas valores 
# da error si le paso solo una llave 