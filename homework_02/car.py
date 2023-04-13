from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine: Engine

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(self, engine):
        self.engine = engine
