from abc import ABC , abstractmethod


class Chain(ABC):
    @abstractmethod
    def setNextChain(self , nextChain):
        pass

    @abstractmethod
    def calculate(self , request):
        pass


class Numbers:
    def __init__(self , newNumber1 , newNumber2 , calcWanted):
        self.number1 = newNumber1
        self.number2 = newNumber2
        self.calculationWanted = calcWanted

    def getNumber1(self):
        return self.number1

    def getNumber2(self):
        return self.number2

    def getCalcWanted(self):
        return self.calculationWanted


class AddNumbers(Chain):
    def setNextChain(self , nextChain):
        self.nextInChain = nextChain

    def calculate(self , request):
        if request.getCalcWanted() == "add":
            print(f"{request.getNumber1()} + {request.getNumber2()} = {request.getNumber1() + request.getNumber2()}")
        else:
            self.nextInChain.calculate(request)


class SubtractNumbers(Chain):
    def setNextChain(self , nextChain):
        self.nextInChain = nextChain

    def calculate(self , request):
        if request.getCalcWanted() == "sub":
            print(f"{request.getNumber1()} - {request.getNumber2()} = {request.getNumber1() - request.getNumber2()}")
        else:
            self.nextInChain.calculate(request)


class MultNumbers(Chain):
    def setNextChain(self , nextChain):
        self.nextInChain = nextChain

    def calculate(self , request):
        if request.getCalcWanted() == "mult":
            print(f"{request.getNumber1()} * {request.getNumber2()} = {request.getNumber1() * request.getNumber2()}")
        else:
            self.nextInChain.calculate(request)


class DivideNumbers(Chain):
    def setNextChain(self , nextChain):
        self.nextInChain = nextChain

    def calculate(self , request):
        if request.getCalcWanted() == "div":
            print(f"{request.getNumber1()} / {request.getNumber2()} = {request.getNumber1() / request.getNumber2()}")
        else:
            print("Only works for add, sub, mult, and div")


class TestCalcChain:
    @staticmethod
    def main():
        # Here I define all of the objects in the chain
        chainCalc1 = AddNumbers()
        chainCalc2 = SubtractNumbers()
        chainCalc3 = MultNumbers()
        chainCalc4 = DivideNumbers()

        # Here I tell each object where to forward the
        # data if it can't process the request
        chainCalc1.setNextChain(chainCalc2)
        chainCalc2.setNextChain(chainCalc3)
        chainCalc3.setNextChain(chainCalc4)

        # Define the data in the Numbers Object
        # and send it to the first Object in the chain
        request = Numbers(4 , 2 , "add")
        chainCalc1.calculate(request)

        request = Numbers(4 , 2 , "sub")
        chainCalc1.calculate(request)

        request = Numbers(4 , 2 , "mult")
        chainCalc1.calculate(request)

        request = Numbers(4 , 2 , "div")
        chainCalc1.calculate(request)

# Test Drive
if __name__ == "__main__":
    TestCalcChain.main()
