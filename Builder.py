from __future__ import annotations
from abc import ABC, abstractmethod

class Builder(ABC):

    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def add_body(self):
        pass

    @abstractmethod
    def add_seats(self):
        pass

    @abstractmethod
    def add_engine(self):
        pass

    @abstractmethod
    def add_roof(self):
        pass

class RangeBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Car()

    @property
    def product(self) -> Car:
        product = self._product
        self.reset()
        return product
    
    def add_body(self):
        self._product.body = "SUV"
        self._product.add("SUV")

    def add_seats(self):
        self._product.seats = "Leather"
        self._product.add("Leather")

    def add_engine(self):
        self._product.engine = "V8"
        self._product.add("V8")

    def add_roof(self):
        self._product.roof = "Sun roof"
        self._product.add("Sun roof")

    def add_smartCar(self):
        self._product.smartCar = "Auto Pilot ENABLED"
        self._product.add("Auto Pilot ENABLED")
    
    def add_goldRims(self):
        self._product.goldRims = "Gold Rims"
        self._product.add("Gold Rims")

class JeepBuilder(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Car()

    @property
    def product(self) -> Car:
        product = self._product
        self.reset()
        return product
    
    def add_body(self):
        self._product.body = "SUV"
        self._product.add("SUV")

    def add_seats(self):
        self._product.seats = "Nylon"
        self._product.add("Nylon")

    def add_engine(self):
        self._product.engine = "V6"
        self._product.add("V6")

    def add_roof(self):
        self._product.roof = "Hard top"
        self._product.add("Hard top")

    def add_smartCar(self):
        self._product.smartCar = "Auto Pilot ENABLED"
        self._product.add("Auto Pilot ENABLED")
    
    def add_goldRims(self):
        self._product.goldRims = "Gold Rims"
        self._product.add("Gold Rims")
     

class Car():

    def __init__(self):
        self.specs = []
        self.body = None
        self.seats = None
        self.engine = None
        self.roof = None
        self.smartCar = None
        self.goldRims = None

    def get_specs(self):
        print(f"This Car's specs are: {', '.join(self.specs)}")

    def add(self, spec):
        self.specs.append(spec)

class Director:
    
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def build_standard_car(self):
        self._builder.add_body()
        self._builder.add_seats()
        self._builder.add_engine()
        self._builder.add_roof()

    def build_premium_car(self):
        self._builder.add_body()
        self._builder.add_seats()
        self._builder.add_engine()
        self._builder.add_roof()
        self.builder.add_smartCar()
        self._builder.add_goldRims()

if __name__ == "__main__":

    director = Director()
    builder1 = RangeBuilder()
    builder2 = JeepBuilder()
    director.builder = builder1

    print("Builing car with the standard specs")
    director.build_standard_car()
    builder1.product.get_specs()

    print("\n")

    print("Building car with the premium specs")
    director.build_premium_car()
    builder1.product.get_specs()

    print("\n")

    print("Builing car with the standard specs")
    director.builder = builder2
    director.build_standard_car()
    builder2.product.get_specs()