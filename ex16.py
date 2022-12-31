from sys import argv 

script, filename = argv # jala el nombre del archivo desde que lo ejecuto y necesito
# darle el nombre del archivo que va a darle truncate

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # abre el archivo para escribir sobre el y primero lo da truncate
# nota: open en modo 'w' escribe pero primero hace un truncate al archivo

print("Truncating the file. Goodbye!")
target.truncate() # ya esta abierto el archivo, le esta dando truncate 
# explicitamente puedo hacerle truncate al archivo, pero cuando lo abri con el modo "w" tambien
# ya le hizo truncate

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) # a traves de .write() esta escribiendo strings en el archivo
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()