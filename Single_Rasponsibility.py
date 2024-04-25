"""
Violate the principle
class Rectangle(object):

    def __init__(self , height: float , width: float):
        self.height = height
        self.width = width

    def draw(self):
        return visual_representation(self)

    def area(self):
        return self.height * self.width
"""

"""
Obey the Principle
class GeometricRectangle(object):

    def __init__(self , height: float , width: float):
        self.height = height
        self.width = width

    def area(self):
        return height * width


class Rectangle(GeometricRectangle):

    def draw(self):
        return visual_representation(self)
"""