def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b 

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b 

def multiply(a, b):
    print(f"Multiplying {a} * {b} ")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b} ")
    return a/b 

print("Let's do some math with just functions!")

age = add(int(input("numero 1 para la edad: ")), int(input("numero dos para la edad: ")))
height = subtract(int(input("numero 1 para la altura ")), int(input("numero dos para la altura: ")) )
weight = multiply(int(input("numero 1 para multiply ")), int(input("numero dos para multiply: ")))
iq = divide(int(input("numero uno para divide: ")), int(input("numero dos para divide")))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")