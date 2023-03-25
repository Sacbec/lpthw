people = 75
cats = 3
dogs = 20

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs :
    print("People are greater than or equal to dogs")
if people <= dogs: 
    print("People are less than or equal to dogs")
if people == dogs:
    print("People are dogs")

if cats > dogs :
    print("There is more cats than dogs")
    if dogs <= people:
        print("there is more people than dogs")
        if people > cats:
            print("Theres more people than cats")
