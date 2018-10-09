#Exercise 1
print("Hello World! ")
print("Hello Again. ")
print("I likek typing this. ")
print("This is fun. ")
print("Yay! Printing. ")
print("I said do not touch this. ")

#Exercise 3
print("I will now count my chickens: ")
print("Hens", 25 + 40 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs. ")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7? " , 3 + 2 < 5 - 7 )
print("What is 3 + 2?" , 3 + 2)
print("What is 5 - 7?" , 5 - 7)
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?" , 5 > -2)
print("Is it greater or equal?" , 5 >= -2)
print("Is it less or equal?" , 5 <= -2)

#Exercise 4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {average_passengers_per_car} in each car.")

from sys import argv
script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
