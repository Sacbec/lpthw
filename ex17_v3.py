from sys import argv
from os.path import exists

script, source, target = argv 

print("Estoy abriendo y escribiendo al mismo tiempo: " )

open(target, 'w').write(open(source).read())