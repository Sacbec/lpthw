formatter = "%r %r %r %r" # string que tiene porcentajes con r
# %r me permite colocar valores ahi
# tambien necesito usar %() con los valores adentro

print( formatter % (1,2,3,4)) # puedo imprimir con porcentaje y seguido de los valores entre parentesis
print( formatter % ('one', 'two', 'three', 'four'))
print( formatter % (True, False, False, True)) 
print( formatter % (formatter, formatter, formatter, formatter)) # si voy a usar % para pasar argumentos,
# necesito darle todos o genera error, en este caso esta imprimiendo '%r' como un string
print( formatter % (
    "I had this thing.", 
    "That you could type up right.", 
    "But it didn't sing.", 
    "So I said goodnight."
))

s_r_differences = "%s %r"
print(s_r_differences % ('al rato podre practicar ingles', 'al rato podre practicar ingles'))
# s lo imprime como usualmente sirve a la lectura humana, 
# r lo imprime con todos sus elementos esto sirve para que los programadores le hagan una inspeccion