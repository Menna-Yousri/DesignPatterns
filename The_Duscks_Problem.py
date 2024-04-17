
class Duck:
    def quack(self):
        print("Quack!")

    def fly(self):
        print("Flying...")

    def eat(self):
        print("Eating...")

    def display(self):
        print("Displaying duck")


class WildDuck(Duck):
    def display(self):
        print("Displaying wild duck")


class CityDuck(Duck):
    def display(self):
        print("Displaying city duck")


class RubberDuck(Duck):
    def fly(self):
        print("Can't fly!")

    def quack(self):
        print("Squeak!")

    def display(self):
        print("Displaying rubber duck")

    def eat(self):
        print("Rubber ducks can't eat!")


class InjuredDuck(Duck):
    def fly(self):
        print("Can't fly!")

    def display(self):
        print("Displaying injured duck")


class MountainDuck(Duck):
    def eat(self):
        print("Fishes!")

    def display(self):
        print("Displaying mountain duck")


class CloudDuck(Duck):
    def eat(self):
        print("Fishes!")

    def display(self):
        print("Displaying cloud duck")


wild_duck = WildDuck()
city_duck = CityDuck()
rubber_duck = RubberDuck()
injured_duck = InjuredDuck()
mountain_duck = MountainDuck()
cloud_duck = CloudDuck()

wild_duck.quack()
wild_duck.fly()
wild_duck.eat()
wild_duck.display()

city_duck.quack()
city_duck.fly()
city_duck.eat()
city_duck.display()

rubber_duck.quack()
rubber_duck.fly()
rubber_duck.display()

injured_duck.quack()
injured_duck.fly()
injured_duck.eat()
injured_duck.display()

mountain_duck.quack()
mountain_duck.fly()
mountain_duck.eat()
mountain_duck.display()

cloud_duck.quack()
cloud_duck.fly()
cloud_duck.eat()
cloud_duck.display()

#Apply the Strategy Pattern for this code