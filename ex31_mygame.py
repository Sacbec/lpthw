def welcome():
    print("""

🥚🐉 Hunting eggs 🐉 🥚

    """)

def grass():
    grass = input("> ")
    if grass == 'walk':
        print("Cool walking around you have encountered an abandoned nest")
    elif grass == 'stay':
        print("Good election. Enjoy the weather and that slowly breeze")
    elif grass == 'look right':
        print("good job! There's a path")
        path = input("> ")
        if path == 'path'or path == 'go' or path == 'yes':
            print("Let's go on the path")
        else:
            print("You came back to admire the mountains view. ")

    elif grass == 'look left':
        print("there are a buch of rocks there")
    else:
        print("ok, when you want to continue just say it...")





def main():
    welcome()
    print("Welcome to this world. You have appeared in a big yard rounded by mountains")
    print("The air is slowly moving the top of the grass")
    while True:
        grass()
        con = input("continue? ")
        if con == 'yes':
            continue 
        else:
            break 


main()
