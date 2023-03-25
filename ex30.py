
people = 37
cars = 29
trucks = 56

if cars > people:
    print("We should take the cars.") 
elif cars < people: 
    print("We should not take the cars.") #
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")#
elif trucks < cars :
    print("Maybe we could take the trucks.") 
else: 
    print("We still can't decide. ")

if people > trucks:
    print("Alright, let's just  take the trucks.") 
else:
    print("Fine, let's stay home then.")#

if trucks > cars  and people > trucks:
    print("there's more people than trucks and cars")
elif cars > people and people < trucks:
    print("there's much cars than people and trucks")
elif trucks > people and people> cars :
    print("there's much trucks than people and cars") #