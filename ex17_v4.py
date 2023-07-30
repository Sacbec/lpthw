from sys import argv 

# objetivo: copiar un archivo en otro
script, filename_source, filename_target = argv 

print("opening source file")
source = open(filename_source, 'r')
content = source.read()
source.close()
print("closing source file")

print("opening target file")
target = open(filename_target, 'w')
print("erasing content")
target.truncate()
print("copying to target")
target.write(content)
print("closing file")
target.close()
print("now you cant check")