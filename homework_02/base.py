import abc
from abc import ABC
import exceptions


class Vehicle(ABC):

    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        max_distance = self.fuel / self.fuel_consumption
        if max_distance >= distance:
            self.fuel -= (max_distance - distance) * self.fuel_consumption
            return True
        else:
            raise exceptions.NotEnoughFuel()

    fuel = 100
    fuel_consumption = 10

    print(move())

