#creates the function cheese_and_crackers, which contains cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket.\n")


#prints the print statements above each time you input the function cheese_and_crackers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
#inputs 20 for cheese_count and 30 for boxes_of_crackers
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
#below redefines cheese_and_crackers, above sets cheese to 10 & crackers to 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#in the function, adds 10 + 20 for cheese and 5 + 6 for crackers
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#adds 100 to 10 previously in amount_of_cheese, adds 1000 to 50 previously in amount_of_crackers
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def boxes_of_balls(penn_balls, wilson_balls, us_open_balls):
    print(f"You have {penn_balls} Penn balls.")
    print(f"You have {wilson_balls} Wilson balls.")
    print(f"You have {us_open_balls} US Open balls.\n")


amount_of_penn = 30
amount_of_wilson = 20
amount_of_us_open = 50


boxes_of_balls(amount_of_penn, amount_of_wilson, amount_of_us_open)
print("With the recently acquired tennis balls:\n")
boxes_of_balls(amount_of_penn + 30, amount_of_wilson + 60, amount_of_us_open + 70)
