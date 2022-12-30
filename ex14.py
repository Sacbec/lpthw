from sys import argv 

script, user_name = argv # desde la terminal voy a pasar una
# variable porque la otra es el nombre del script  y ese mismo
# lo usa para la primera variable 
prompt = '---> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) #aqui le pide una respuesta al usuario

print(f"Where do you live {user_name}?")
lives = input(prompt) # el mensaje del input es 
# lo que contiene la variable prompt
# es util en el sentido de que si quiero cambiar el mensaje
# solo modifico la variable y no cada parte del input

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
    Alright, so you said {likes} about linking me.
    You live in {lives}. Not sure where that is. 
    And you have a {computer} computer. Nice. 
 """)

 