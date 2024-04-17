class IFlyBehavior:
    def fly(self):
        pass

class CanFly(IFlyBehavior):
    def fly(self):
        print("Flying...")

class CannotFly(IFlyBehavior):
    def fly(self):
        print("Can't fly!")


class IQuackBehavior:
    def quack(self):
        pass

class Quack(IQuackBehavior):
    def quack(self):
        print("Quack!")

class Squeak(IQuackBehavior):
    def quack(self):
        print("Squeak!")

class IDisplayBehavior:
    def display(self):
        pass

class Graph(IDisplayBehavior):
    def display(self):
        print("Graph display!")

class Text(IDisplayBehavior):
    def display(self):
        print("Text display!")

class Duck:
    def __init__(self, fly_behavior, quack_behavior, display_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior
        self.display_behavior = display_behavior

    def perform(self):
        self.fly_behavior.fly()
        self.quack_behavior.quack()
        self.display_behavior.display()

noFly= CannotFly()
quack= Quack()
text= Text()
injuredDuck= Duck(noFly, quack, text)
injuredDuck.perform()
