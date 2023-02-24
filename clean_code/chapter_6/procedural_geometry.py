from typing import final

from clean_code.chapter_6.data_abstraction import Point


class Square:
    top_left: Point
    side: float


class Rectangle:
    top_left: Point
    height: float
    width: float


class Circle:
    center: Point
    radius: float


class Geometry:
    PI: final[float] = 3.141592653589793

    def area(self, shape_object: object) -> float:
        if isinstance(shape_object, Square):
            return shape_object.side * shape_object.side
        elif isinstance(shape_object, Rectangle):
            return shape_object.height * shape_object.width
        elif isinstance(shape_object, Circle):
            return self.PI * shape_object.radius * shape_object.radius
        else:
            raise TypeError("Unknown shape object")
