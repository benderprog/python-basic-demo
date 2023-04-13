from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_weight):
        full_weight = cargo_weight + self.cargo
        if full_weight <= self.max_cargo:
            self.cargo += cargo_weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        result = self.cargo
        self.cargo = 0
        return result
