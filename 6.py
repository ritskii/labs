#Варіант 2
#• Абстрактний клас Vehicle з методом move().
#• Реалізуйте класи Car, Bicycle, Airplane, які реалізують цей метод.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


class Airplane(Vehicle):
    def move(self):
        return "Airplane is flying"


print(Car().move())
print(Bicycle().move())
print(Airplane().move())
