class Tea:
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        print("Steeping the tea")

    def pour_in_cup(self):
        print("Pouring water into the cup")

    def add_condiments(self):
        print("Adding lemon")


class Coffee:
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        print("Dripping coffee through filter")

    def pour_in_cup(self):
        print("Pouring water into the cup")

    def add_condiments(self):
        print("Adding sugar and milk")

if __name__ == "__main__":
    print("Preparing Tea:")
    tea = Tea()
    tea.prepare()

    print("\nPreparing Coffee:")
    coffee = Coffee()
    coffee.prepare()


