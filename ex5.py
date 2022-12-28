name = 'Zed A. Shaw'
age = 35 # not a lie 
height  = 74 # inches
weight = 180 # lbs
eyes = 'Blue' 
teeth = 'White'
hair = 'Brown'
def pounds_to_kgs (weight):
    kgs = weight * 0.453592
    return kgs
def inches_to_cm(height):
    cms = height * 2.54
    return cms

print(f"Let's talk about {name}.")
print(f"He's {inches_to_cm(height)} centimeters tall.")
print(f"He's {height} inches tall.")
print(f"He's {pounds_to_kgs(weight)} kgs heavy")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} dependending on the coffee.")


total = age + height + weight 
print(f"If I add {age}, {height}, and {weight} I get {total}")
