from abc import ABC, abstractmethod

class BeverageMaker(ABC):
    # Template method defining the overall process
    # Template method defines the skeleton of an algorithm.
    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    # Abstract methods to be implemented by subclasses
    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    # Common methods
    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

class Tea(BeverageMaker):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

class Coffee(BeverageMaker):
    def brew(self):
        print("Dripping coffee through filter")

    def add_condiments(self):
        print("Adding sugar and milk")

if __name__ == "__main__":
    print("Preparing Tea:")
    tea = Tea()
    tea.make_beverage()

    print("\nPreparing Coffee:")
    coffee = Coffee()
    coffee.make_beverage()
