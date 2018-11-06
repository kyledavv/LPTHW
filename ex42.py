## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal?
class Dog(Animal):

    def __init__(self, name):
        ## ?
        self.name = name

## ?
class Cat(Animal):

    def __init__(self, name):
        ## ?
        self.name = name

## ?
class Person(object):

    def __init__(self, name):
        ## person has-a name?
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ?
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ?
        self.salary = salary

## Fish is-a object?
class Fish(object):
    pass

## Salmon is-a Fish?
class Salmon(Fish):
    pass

## Halibut is-a Fish?
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat?
satan = Cat("Satan")

## Mary is-a Person?
mary = Person("Mary")

## ?
mary.pet = satan

## ?
frank = Employee("Frank", 120000)

## ?
frank.pet = rover

## Fish has-a flipper?
flipper = Fish()

## Salmon has-a crouse?
crouse = Salmon()

## harry is-a halibut???????
harry = Halibut()
