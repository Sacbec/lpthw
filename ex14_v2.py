from sys import argv

archivo, autor, edad, fecha = argv 

prompt = ':D '

print(f"Hi {autor}, I'm the {archivo} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {autor}?")
likes = input(prompt)

print(f"Where do you live {autor}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)



print(f"""
    Alright, so you said {likes} about liking me. 
    You live in {lives}. Not sure where that is.
    And you have a {computer} computer. Nice.
    Also today is {fecha} y tienes {edad} años. 
    """)