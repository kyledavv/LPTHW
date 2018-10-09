name = 'Kyle J. Davidson'
age = 23 # the truth
height = 73 # inches
weight = 200 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy. ")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
height_centi = round(height * 2.54)
weight_kilo = round(weight * .45359237)
print(f"According to the correct conversions, I am {height_centi} centimeters tall")
print(f"and {weight_kilo} kilograms heavy.")
