from two_d_shape import TwoDimensionalShape
from math import pi

class Circle(TwoDimensionalShape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("radius::", self.radius)
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius * self.radius
