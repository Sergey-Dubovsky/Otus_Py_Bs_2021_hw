"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload 

class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self,new_cargo):
        if self.cargo+new_cargo < self.max_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload
    
    def remove_all_cargo(self):
        result=self.cargo
        self.cargo=0
        return result

