from abc import ABC, abstractmethod

class BeverageMaker(ABC):
    def __init__(self, use_condiments=True):
        self.use_condiments = use_condiments

    # Template method defining the overall process
    # Template method defines the skeleton of an algorithm.
    def make_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        # These are "hooks." Subclasses may override them, but it's not mandatory
        # since the hooks already have default (but empty) implementation. Hooks
        # provide additional extension points in some crucial places of the
        # algorithm.
        if self.use_condiments:
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
    tea = Tea(True)
    tea.make_beverage()

    print("\nPreparing Tea (without condiments):")
    tea = Tea(False)
    tea.make_beverage()
