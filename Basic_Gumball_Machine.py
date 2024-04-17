class GumballMachine:
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3

    def __init__(self, count):
        self.state = self.SOLD_OUT
        self.count = count
        if count > 0:
            self.state = self.NO_QUARTER

    def insertQuarter(self):
        if self.state == self.HAS_QUARTER:
            print("You can't insert another quarter")
        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print("You inserted a quarter")
        elif self.state == self.SOLD_OUT:
            print("You can't insert a quarter, the machine is sold out")
        elif self.state == self.SOLD:
            print("Please wait, we’re already giving you a gumball")

    def ejectQuarter(self):
        if self.state == self.HAS_QUARTER:
            print("Quarter returned")
            self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You haven’t inserted a quarter")
        elif self.state == self.SOLD:
            print("Sorry, you already turned the crank")
        elif self.state == self.SOLD_OUT:
            print("You can't eject, you haven’t inserted a quarter yet")

    def turnCrank(self):
        if self.state == self.SOLD:
            print("Turning twice doesn’t get you another gumball!")
        elif self.state == self.NO_QUARTER:
            print("You turned but there’s no quarter")
        elif self.state == self.SOLD_OUT:
            print("You turned, but there are no gumballs")
        elif self.state == self.HAS_QUARTER:
            print("You turned...")
            self.state = self.SOLD
            self.dispense()

    def dispense(self):
        if self.state == self.SOLD:
            print("A gumball comes rolling out the slot")
            self.count -= 1
            if self.count == 0:
                print("Oops, out of gumballs!")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER
        elif self.state == self.NO_QUARTER:
            print("You need to pay first")
        elif self.state == self.SOLD_OUT:
            print("No gumball dispensed")
        elif self.state == self.HAS_QUARTER:
            print("No gumball dispensed")

    def refill(self, count):
        self.count += count
        print("The gumball machine was just refilled; its new count is:", self.count)
        if self.state == self.SOLD_OUT:
            self.state = self.NO_QUARTER

    def __str__(self):
        result = "Inventory: " + str(self.count) + " gumball"
        if self.count != 1:
            result += "s"
        result += "\n"
        result += "Machine is " + str(self.state) + "\n"
        return result


if __name__ == "__main__":
    gumballMachine = GumballMachine(2)

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)

    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    gumballMachine.refill(5)
    gumballMachine.insertQuarter()
    gumballMachine.turnCrank()

    print(gumballMachine)
