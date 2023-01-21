# replicate 24 + 34 / 100 - 1023

def add(a, b):
    print(f"I'm adding {a} with {b}")
    return a + b

def divide(a, b):
    print(f"I'm dividing {a} and {b}")
    return a/b 

def subtract(a, b):
    print(f"I'm  doing {a} - {b}")
    return a - b 

print("The result is: ",  add(24, subtract(divide(34, 100), 1023)  ) )