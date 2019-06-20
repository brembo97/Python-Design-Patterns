from abc import ABC, abstractclassmethod

class Transport(ABC):
    
    def __init__(self):
        self.locations = []

    @abstractclassmethod
    def makeDelivery(self, location):
        pass
    
    @abstractclassmethod
    def getType(self):
        pass

    def getLocations(self):
        return self.locations
    
    def addLocation(self, newLocation):
        self.locations.append(newLocation)

class Ship(Transport):

    def __init__(self):
        self.locations = ["Jamaica", "Cape Town"]

    def makeDelivery(self, locations):
        for location in locations:
            print(f"Making a naval delivery to {location}")
    
    def getType(self):
        print(f"Carrying your package on a ship")

class Plane(Transport):

    def __init__(self):
        self.locations = ["Moscu", "Hong Kong"]

    def makeDelivery(self, locations):
        for location in locations:
            print(f"Making an aerial delivery to {location}")
    
    def getType(self):
        print(f"Carrying your package on a plane")    

class Truck(Transport):

    def __init__(self):
        self.locations = ["Sao Paulo", "Texas"]

    def makeDelivery(self, locations):
        for location in locations:
            print(f"Making a terrestrial delivery to {location}")
    
    def getType(self):
        print(f"Carrying your package on a truck")

class Logistics(ABC):

    def __init__(self):
        self.createTransport()

    @abstractclassmethod
    def createTransport(self):
        pass 


class LandLogistics(Logistics):
    
    def createTransport(self):
        return Truck()

class OceanLogistics(Logistics):

    def createTransport(self):
        return Ship()

class AirLogistics(Logistics):

    def createTransport(self):
        return Plane()

if __name__ == "__main__":
    
    Logistic1 = OceanLogistics().createTransport()
    Logistic1.getType()
    Logistic1.addLocation("Hawaii")
    Logistic1.makeDelivery(Logistic1.getLocations())

