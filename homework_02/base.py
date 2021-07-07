from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload 

class Vehicle:

    def __init__(self, weight=2000, fuel=0, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False


    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError  

    def move(self,distance):
        if self.fuel < (distance * self.fuel_consumption):
            raise NotEnoughFuel
        else:
             self.fuel -= (distance * self.fuel_consumption)
            
