days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months) # cuando meto la palabra clave \n python hara un salto de linea

print("""
    There's somenthing going on here. 
    With the three double-quotes. 
    We'll be able to type as much as we like. 
    Even 4 lines if we want, or 5, or 6. 
""")

# que pasa si le doy espacio a los saltos de linea
# respuesta: nada, puedo poner el salto de linea pegado o
# dandole su espacio para que sea legible y aun asi se ejecuta

months2 = "Jan \n Feb \n Mar \n Apr \n May \n Jun \n Jul \n Aug"

print("Here are the months2: ", months2)

# quiero empezar los meses en una nueva linea

print("Here are the months with space: ", '\n' + months)