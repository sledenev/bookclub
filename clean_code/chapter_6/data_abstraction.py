import abc
from dataclasses import dataclass


@dataclass
class Point:
    """
    Listing 6-1. The Point class

    Listing 6-1, on the other hand, is very clearly implemented in rectangular
    coordinates, and it forces us to manipulate those coordinates independently.
    This exposes implementation. Indeed, it would expose implementation even if
    the variables were private and we were using single variable getters and setters.
    """
    x: float
    y: float


class AbstractPoint(abc.ABC):
    """
    Listing 6-2. The AbstractPoint class

    The beautiful thing about Listing 6-2 is that there is no way you can tell whether
    the implementation is in rectangular or polar coordinates. It might be neither!
    And yet the interface still unmistakably represents a data structure.

    But it represents more than just a data structure. The methods enforce an access policy.
    You can read the individual coordinates independently, but you must set the
    coordinates together as an atomic operation.
    """
    @abc.abstractmethod
    def get_x(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_y(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def set_cartesian(self, x: float, y: float) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_r(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def get_theta(self) -> float:
        raise NotImplementedError

    @abc.abstractmethod
    def set_polar(self, r: float, theta: float) -> None:
        raise NotImplementedError


class VehicleConcrete:
    """
    Listing 6-3. The Vehicle class

    Here we have a class that is clearly implemented in terms of fuel.
    It exposes the implementation of the fuel tank.
    """

    def get_fuel_tank_capacity_in_gallons(self) -> float:
        raise NotImplementedError

    def get_gallons_of_fuel_in_tank(self) -> float:
        raise NotImplementedError


class VehicleAbstract:
    """
    Listing 6-4. The Vehicle class

    The Vehicle class in Listing 6-4 is a much better design.
    It hides the implementation of the fuel tank.
    """
    def get_percent_fuel_remaining(self) -> float:
        raise NotImplementedError