import abc
from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    """
    доработайте базовый класс base.Vehicle:
    добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    """
    def __init__(self, weight: float, fuel: float, fuel_consumption: float):
        """
        добавьте инициализатор для установки weight, fuel, fuel_consumption
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        """
        Добавьте метод start. При вызове этого метода необходимо проверить состояние started.
        И если не started, то нужно проверить, что топлива больше нуля, и обновить состояние started,
        иначе нужно выкинуть исключение exceptions.LowFuelError
        """
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                self.started = False
                raise LowFuelError()

    def move(self, distance):
        """
        добавьте метод move, который проверяет, что топлива достаточно для преодоления переданной дистанции
        (вплоть до полного расхода), и изменяет количество оставшегося топлива,
        иначе выкидывает исключение exceptions.NotEnoughFuel
        :param distance:
        :return:
        """
        max_distance = self.fuel / self.fuel_consumption
        if max_distance <= 0:
            raise NotEnoughFuel()
        elif max_distance < distance:
            raise NotEnoughFuel()
        else:
            self.fuel -= distance * self.fuel_consumption
            return self.fuel


# new_vehicle = Vehicle(500, 10, 1)
# result = new_vehicle.move(11)
# print(result, new_vehicle.fuel)
