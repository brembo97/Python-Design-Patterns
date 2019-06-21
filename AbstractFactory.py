from __future__ import annotations
from abc import ABC, abstractmethod

class Trattoria(ABC):

    @abstractmethod
    def createPasta(self) -> Pasta:
        pass

    @abstractmethod
    def createPizza(self) -> Pizza:
        pass

class MeatFactory(Trattoria):

    def createPizza(self) -> MeatLoversPizza:
        return MeatLoversPizza()

    def createPasta(self) -> BolognesePasta:
        return BolognesePasta()

class VeganFactory(Trattoria):

    def createPizza(self) -> VeggiePizza:
        return VeggiePizza()

    def createPasta(self) -> ZucchiniPasta:
        return ZucchiniPasta()

class Pasta(ABC):

    def __init__(self, type):
        self.type = type;

    @abstractmethod
    def getType(self):
        return self.type

    @abstractmethod
    def prepare(self):
        pass

class ZucchiniPasta(Pasta):
    
    def __init__(self, type='Spaghetti'):
        super().__init__(type)

    def getType(self):
        return self.type

    def prepare(self):
        print(f"\tPreparing a " + type(self).__name__ + " on a" + self.type)

class BolognesePasta(Pasta):
    
    def __init__(self, type='Fettuccine'):
        super().__init__(type)

    def getType(self):
        return self.type

    def prepare(self):
        print(f"\tPreparing a " + type(self).__name__ + " on a " + self.type)

class Pizza(ABC):
    
    def __init__(self, type):
        self.type = type;

    @abstractmethod
    def getType(self):
        return self.type

    @abstractmethod
    def cook(self):
        pass

class MeatLoversPizza(Pizza):

    def __init__(self, type='Thick Crust'):
        super().__init__(type)

    def getType(self):
        return self.type

    def cook(self):
        print(f"\tCooking a " + type(self).__name__ + " on a " + self.type)

class VeggiePizza(Pizza):

    def __init__(self, type='Thin Crust'):
        super().__init__(type)

    def getType(self):
        return self.type

    def cook(self):
        print(f"\tCooking a " + type(self).__name__ + " on a " + self.type)

def clientCode(factory : Trattoria):

    pasta = factory.createPasta()
    pizza = factory.createPizza()

    pasta.prepare()
    pizza.cook()

if __name__ == "__main__":

    print("Creating the products of the Vegan Fabric : ")
    clientCode(VeganFactory())

    print("\n")

    print("Creating the prodcuts of the Meat Fabric : ")
    clientCode(MeatFactory())