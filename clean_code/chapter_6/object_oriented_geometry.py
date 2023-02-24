import abc
from abc import ABC
from typing import final

from clean_code.chapter_6.data_abstraction import Point


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float:
        raise NotImplementedError


class Square(Shape):
    top_left: Point
    side: float

    def area(self) -> float:
        return self.side * self.side


class Rectangle(Shape):
    top_left: Point
    height: float
    width: float

    def area(self) -> float:
        return self.height * self.width


class Circle(Shape):
    PI: final[float] = 3.141592653589793
    center: Point
    radius: float

    def area(self) -> float:
        return self.PI * self.radius * self.radius
