people = 20
cars = 20
trucks = 20

#cars > people: take cars. cars < people: not take cars. cars == people: can't decide
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

#trucks > cars: too many trucks. trucks < cars: take trucks. trucks == cars: cant decide
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

#people > trucks: take trucks. otherwise, stay home
if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if people <= cars or trucks >= cars:
    print("Well damn, looks like cars are winning.")
else:
    print("Trucks will rule the world.")
