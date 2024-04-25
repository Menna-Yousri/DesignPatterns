from abc import ABC,abstractmethod
"""class GeometricInterface(ABC):

    @abstractmethod
    def get_area(self):
        raise NotImplementedError

    @abstractmethod
    def get_diameter(self):
        raise NotImplementedError


class Square(GeometricInterface):

    def __init__(self , height: float , width: float):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def get_diameter(self) -> float:
        raise NotImplementedError


class Circle(GeometricInterface):

    def __init__(self , radius: float):
        self.radius = radius

    def get_area(self):
        return self.radius * PI ** 2

    def get_diameter(self) -> float:
        return self.radius * 2
"""

"""
class GeometricInterface(ABC):

    @abstractmethod
    def get_area(self) -> float:
        raise NotImplementedError


class ElipseInterface(GeometricInterface , ABC):

    @abstractmethod
    def get_diameter(self) -> float:
        raise NotImplementedError


class RectangleInterface(GeometricInterface , ABC):
    pass


class Square(RectangleInterface):

    def __init__(self , height: float , width: float):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width


class Circle(ElipseInterface):

    def __init__(self , radius: float):
        self.radius = radius

    def get_area(self):
        return self.radius * PI ** 2

    def get_diameter(self) -> float:
        return self.radius * 2
"""