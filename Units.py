from abc import ABC, abstractmethod
from math import pi


class Unit(ABC):
    @abstractmethod
    def return_k(self): pass


class Centimeter(Unit):
    k = 1

    def return_k(self):
        return self.k


class Ticks(Unit):
    k = None

    def __init__(self, tpr: float, wheel_diameter: float):
        self.__tpr = tpr
        self.__wheel_diameter = wheel_diameter
        self.k = self.__tpr / (pi * self.__wheel_diameter)

    def get_wheel_d(self):
        return self.__wheel_diameter

    def set_wheel_d(self, wheel_diameter):
        self.__wheel_diameter = wheel_diameter
        self.k = self.__tpr / (pi * self.__wheel_diameter)

    def get_tpr(self):
        return self.__tpr

    def set_tpr(self, tpr):
        self.__tpr = tpr
        self.k = self.__tpr / (pi * self.__wheel_diameter)

    wheel_diameter = property(get_wheel_d, set_wheel_d)
    tpr = property(get_tpr, set_tpr)

    def return_k(self):
        return self.k


class Degrees(Unit):
    angle_k = 1

    def return_k(self):
        return self.angle_k


class Radians(Unit):
    angle_k = 180 / pi

    def return_k(self):
        return self.angle_k
