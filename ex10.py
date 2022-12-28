tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """ 
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass

"""
# notar como puedo escribir de corrido sobre la misma linea
# por ejemplo una lista y aun hacer que se imprima con salto de linea
# solo debo agrefar \n y para centrarlo \t

print(tabby_cat) # centra el texto \t
print(persian_cat) # salto de linea \n
print(backslash_cat) # no estoy seguro porque ignora un \
# respuesta: lo que ocurre es que \\ es una combinacion clave
# que muestra un solo \
print(fat_cat)
print("algo\f")
print("ASCII BELL: \a")
print("algo\b")
print("algo\\")
print("algo\'")
print("algo\"")
# print("algo\N{name}")
print("algo\r")
print("algo\t")
# print("algo\uxxxx")
# print("algo\Uxxxxxxxx")
print("algo\v")
print("algo\000")
# print("algo\xhh")
