"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverLoad

class Plane(Vehicle):       #класс Plane должен быть наследником Vehicle
    """
    в модуле plane создайте класс Plane
    класс Plane должен быть наследником Vehicle
    добавьте атрибуты cargo и max_cargo классу Plane
    """
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        """
        добавьте max_cargo в инициализатор (переопределите родительский)
        :param max_cargo:
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.max_cargo = max_cargo
        self.cargo = max_cargo



    def load_cargo(self, cargo_weight):
        """
        объявите метод load_cargo, который принимает число, проверяет,
        что в сумме с текущим cargo не будет перегруза, и обновляет значение,
        в ином случае выкидывает исключение exceptions.CargoOverload
        :param weight:
        :return:
        """
        full_weight = cargo_weight + self.cargo
        if full_weight <= self.max_cargo:
            self.cargo += cargo_weight
        else:
            raise CargoOverLoad()


    def remove_all_cargo(self):
        """
        объявите метод remove_all_cargo, который обнуляет значение cargo и
        возвращает значение cargo, которое было до обнуления
        :param cargo:
        :return:
        """
        result = self.cargo
        self.cargo = 0
        return result
